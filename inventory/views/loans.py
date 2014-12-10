# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from inventory.models import Administrator, Client, Loan
from inventory.forms.loan_form import LoanForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from inventory.views.user import isAdmin

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
	LoanFormSet = modelform_factory(Loan, form=LoanForm)
	if request.method == 'POST':
	    formset = LoanFormSet(request.POST)
	    if formset.is_valid():
	        formset.save()
	        return HttpResponseRedirect('/list_loans')
	        # do something.
	else:
	    formset = LoanFormSet()
	return render_to_response("loans_form.html", {
	    							"form": formset,
								}, context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def return_loan(request, id_loan):
	loan = get_object_or_404(Loan, pk=id_loan)
	loan.cancel()
	return HttpResponseRedirect('/list_loans')

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def loan_cancel_list(request):
	clients = Client.objects.all()
	return render_to_response("loans_cancel_list.html",{"clients":clients},context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def loan_cancel_list_ajax(request):
	if request.method == 'GET':
		id_client = request.GET['id']
		loans = Loan.objects.filter( client = Client.objects.get(id=id_client))
		data = serializers.serialize('json', loans, fields=('item'))
		return HttpResponse(data, content_type='application/json')
