# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from inventory.models import Item
from inventory.models import Administrator
from inventory.models import Location
from inventory.models import Loan
from inventory.forms.item_form import ItemForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import user_passes_test
from inventory.views.user import isAdmin
from django.core import serializers
import json

def item(request, id_item):
	item = get_object_or_404(Item, pk=id_item)
	item.availables = item.stock - Loan.objects.filter(item=item, is_active =True).count() 
	return render_to_response('item.html',{'item':item, 'isAdmin':isAdmin(request.user)}, context_instance=RequestContext(request))
	
@login_required
def list_items(request):
	items = Item.objects.all()
	for item in items:
		item.availables = item.stock - Loan.objects.filter(item=item, is_active =True).count() 
	return render_to_response('items_list.html',{'items':items,'isAdmin':Administrator.objects.filter( user = request.user).exists(),}, context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def register_item(request):
	ItemFormSet = modelform_factory(Item, form=ItemForm)
	if request.method == 'POST':
	    formset = ItemFormSet(request.POST,request.FILES)
	    if formset.is_valid():
	    		handle_uploaded_file(request.FILES['photo'])
	        formset.save()
	        return HttpResponseRedirect('/list_items')
	else:
	    formset = ItemFormSet()
	return render_to_response("items_form.html", {"form": formset,}, context_instance=RequestContext(request))


@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def edit_item(request, id_item):
	item = get_object_or_404(Item, pk=id_item)
	ItemFormSet = modelform_factory(Item, form=ItemForm)
	
	if request.method == 'POST':
	    formset = ItemForm(request.POST, instance=item)
	    if formset.is_valid():
	        formset.save()
	        
	        return HttpResponseRedirect('/list_items')
	else:
	    formset = ItemFormSet(instance = item )
	return render_to_response("items_edit.html", {"form": formset,"item":item}, context_instance=RequestContext(request))
	
@login_required
def search_item(request):
	locations = Location.objects.all()
	return render_to_response("items_search.html", {'locations':locations},context_instance=RequestContext(request))
	
@login_required
def search_item_ajax(request):
	item_filter = {}
	name = request.GET.get('name')
	item_type = request.GET.get('item_type')
	location = request.GET.get('location')
	sublocation = request.GET.get('sublocation')
	isAvailable = request.GET.get('available')
	set_if_not_none(item_filter, 'name__contains', name)
	set_if_not_none(item_filter, 'item_type', item_type)
	set_if_not_none(item_filter, 'location', location)
	set_if_not_none(item_filter, 'sublocation', sublocation)
	items = []
	if isAvailable == 'true':
		for item in Item.objects.filter(**item_filter):
			if item.stock - Loan.objects.filter(item=item, is_active =True).count() > 0:
				items.append(item)
	else:
		items = Item.objects.filter(**item_filter)
	data = []
	for item in items:
		data.append({
			'name' 		: item.name,
			'item_type'	: item.item_type,
			'stock'		: item.stock,
			'availables': item.stock - Loan.objects.filter(item=item, is_active =True).count(),
			'sublocation': item.sublocation,
			'pk'		: item.id
			}
		)
	datas = json.dumps(data)
	return HttpResponse(datas, content_type='application/json')

def set_if_not_none(mapping, key, value):
    if value != 'all' and value != "":
        mapping[key] = value