#from django.shortcuts import render
# -*- coding: utf-8 -*-
from inventory.models import Item
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def items(request):
	html = "<html><body>PROBANDDO</body></html>"
	return HttpResponse(html)
	
def lista_items(request):
	items = Item.objects.all()
	return render_to_response('lista_items.html',{'items':items}, context_instance=RequestContext(request))
	