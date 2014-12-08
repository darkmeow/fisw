# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from inventory.models import Item
from inventory.models import Administrator, Client, Location, Loan
from inventory.forms.item_form import ItemForm
from inventory.forms.location_form import LocationForm
from inventory.forms.loan_form import LoanForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.core import serializers


def location(request):
	html = "<html><body>PROBANDDO</body></html>"
	return HttpResponse(html)


def wcg_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			login(request, user)
			if user.is_superuser:
				return HttpResponseRedirect('/admin')
			else:
				return HttpResponseRedirect('/dashboard')
		else:
			#disabled page
			pass
	else:
		return HttpResponseRedirect('/')
	
@login_required
def dashboard(request):

	if Administrator.objects.filter( user = request.user).exists():
		print Administrator.objects.filter( user = request.user)
		return render_to_response('dashboard_admin.html', context_instance=RequestContext(request))
	elif Client.objects.filter(user = request.user).exists():
		return render_to_response('dashboard_client.html', context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def index(request):
	if request.user.is_authenticated():
		#Logged in
		if request.user.is_superuser:
			#As a super user
			return HttpResponseRedirect('/admin')
		#As a system user
		return HttpResponseRedirect('/dashboard')
	return render_to_response('index.html', context_instance=RequestContext(request))


def item(request, id_item):
	item = get_object_or_404(Item, pk=id_item)
	return render_to_response('item.html',{'item':item,}, context_instance=RequestContext(request))
	
def loan(request, id_loan):
	
	loan = get_object_or_404(Loan, pk=id_loan)
	return render_to_response('loan.html',{'loan':loan,}, context_instance=RequestContext(request))


######################################################################################################
@login_required
def list_items(request):
	items = Item.objects.all()
	return render_to_response('items_list.html',{'items':items,'isAdmin':Administrator.objects.filter( user = request.user).exists(),}, context_instance=RequestContext(request))

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
	
######################################################################################################

@login_required
def register_item(request):
	if Administrator.objects.filter( user = request.user).exists():
		ItemFormSet = modelform_factory(Item, form=ItemForm)
		if request.method == 'POST':
		    formset = ItemFormSet(request.POST)
		    if formset.is_valid():
		        formset.save()
		        return HttpResponseRedirect('/list_items')
		else:
		    formset = ItemFormSet()
		return render_to_response("items_form.html", {"form": formset,}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/dashboard')

@login_required	
def register_loan(request):
	if Administrator.objects.filter( user = request.user).exists():
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
	else:
		return HttpResponseRedirect('/dashboard')
		
@login_required
def return_loan(request, id_loan):
	if Administrator.objects.filter( user = request.user).exists():
		loan = get_object_or_404(Loan, pk=id_loan)
		loan.cancel()
		return HttpResponseRedirect('/list_loans')
	else:
		return HttpResponseRedirect('/dashboard')
		
@login_required
def loan_cancel_list(request):
	if Administrator.objects.filter( user = request.user).exists():
		clients = Client.objects.all()
		return render_to_response("loans_cancel_list.html",{"clients":clients},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/dashboard')

@login_required
def loan_cancel_list_ajax(request):
	if Administrator.objects.filter( user = request.user).exists():
		if request.method == 'GET':
			id_client = request.GET['id']
			loans = Loan.objects.filter( client = Client.objects.get(id_client))
			data = serializers.serialize('json', loans, fields=('item'))
			return HttpResponse(data, mimetype='application/json')
	return False
		