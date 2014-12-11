# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from inventory.models import Administrator, Client, Loan, Project
from inventory.forms.loan_form import LoanForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from inventory.views.user import isAdmin
from django.utils import timezone
import json
def loan(request, id_loan):
	loan = get_object_or_404(Loan, pk=id_loan)
	return render_to_response('loan.html',{'loan':loan,}, context_instance=RequestContext(request))

@login_required
def list_loans(request):
	if Administrator.objects.filter( user = request.user).exists():
		loans = Loan.objects.filter(is_active = True)
	elif Client.objects.filter(user = request.user).exists():
		loans = Loan.objects.filter(client = Client.objects.filter(user = request.user)).filter(is_active = True)
	else:
		return HttpResponseRedirect('/login')
#	loans = Loan.objects.all()
	return render_to_response('loans_list.html',{'loans':loans,'isAdmin':Administrator.objects.filter( user = request.user).exists()}, context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def register_loan(request):
	not_available = False
	LoanFormSet = modelform_factory(Loan, form=LoanForm)
	if request.method == 'POST':
	    formset = LoanFormSet(request.POST)
	    if formset.is_valid():
	        instance = formset.save(commit=False)
	        if instance.item.stock - Loan.objects.filter(item=instance.item, is_active =True).count() <= 0:
	        	not_available = True
	        else:	
	        	instance.loan_date = timezone.now()
	        	instance.save()
		        return HttpResponseRedirect('/list_loans')
		        # do something.
	else:
	    formset = LoanFormSet()
	return render_to_response("loans_form.html", {
	    							"form": formset, "not_available": not_available
								}, context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def return_loan(request, id_loan):
	loan = get_object_or_404(Loan, pk=id_loan)
	loan.cancel()
	return HttpResponseRedirect('/loan_cancel_list')

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def loan_cancel_list(request):
	clients = Client.objects.all()
	projects = Project.objects.all()
	return render_to_response("loans_cancel_list.html",{"clients":clients, "projects": projects},context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def loan_cancel_list_ajax(request):
	if request.method == 'GET':
		id_client = request.GET['client']
		id_project = request.GET['project']
		if id_client != 'all':
			loans = Loan.objects.filter( client = Client.objects.get(id=id_client), is_active=True)
		elif id_project != 'all':
			loans = Loan.objects.filter(client__project = id_project, is_active = True)
		else:
			loans = Loan.objects.filter(is_active= True)
		
		data = []
		for loan in loans:
			data.append({
				'client' 	: loan.client.user.first_name + ' ' +loan.client.user.last_name,
				'item'		: loan.item.name,
				'date'		: loan.loan_date.strftime("%d/%m/%y %H:%M:%S"),
				'pk'		: loan.id
				}
			)
		#data = serializers.serialize('json', loans, fields=('client__user__first_name','item', 'loan_date'))
		datas = json.dumps(data)
		return HttpResponse(datas, content_type='application/json')

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def loan_history(request):
	loans = Loan.objects.all().order_by('-loan_date')
	return render_to_response("loans_history.html",{"loans":loans},context_instance=RequestContext(request))


@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def get_loans(request):

	loans = Loan.objects.all()
	
	graph = []
	for loan in loans:
		graph.append({
			'item'			: loan.item.name,
			'client' 		: loan.client.user.first_name + ' ' +loan.client.user.last_name,
			'date'			: loan.loan_date.strftime("%d/%m/%y %H:%M:%S"),
			'return_date'	: loan.return_date.strftime("%d/%m/%y %H:%M:%S"),
			'pk'			: loan.id
			}
		)
	graphs = json.dumps(graph)
	return HttpResponse(graphs, content_type='application/json')
