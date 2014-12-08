# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from inventory.models import Item
from inventory.models import Administrator
from inventory.forms.item_form import ItemForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import user_passes_test
from inventory.views.user import isAdmin

def item(request, id_item):
	item = get_object_or_404(Item, pk=id_item)
	return render_to_response('item.html',{'item':item,}, context_instance=RequestContext(request))
	
@login_required
def list_items(request):
	items = Item.objects.all()
	return render_to_response('items_list.html',{'items':items,'isAdmin':Administrator.objects.filter( user = request.user).exists(),}, context_instance=RequestContext(request))

@user_passes_test(lambda u: isAdmin(u), '/dashboard')
def register_item(request):
	ItemFormSet = modelform_factory(Item, form=ItemForm)
	if request.method == 'POST':
	    formset = ItemFormSet(request.POST)
	    if formset.is_valid():
	        formset.save()
	        return HttpResponseRedirect('/list_items')
	else:
	    formset = ItemFormSet()
	return render_to_response("items_form.html", {"form": formset,}, context_instance=RequestContext(request))


