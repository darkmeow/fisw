# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from inventory.models import Item
from inventory.models import Administrator, Client
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
def location(request):
	html = "<html><body>PROBANDDO</body></html>"
	return HttpResponse(html)

@login_required
def lista_items(request):
	items = Item.objects.all()
	return render_to_response('lista_items.html',{'items':items}, context_instance=RequestContext(request))

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
		if request.user.is_superuser:
			return HttpResponseRedirect('/admin')
		return HttpResponseRedirect('/dashboard')
	return render_to_response('index.html', context_instance=RequestContext(request))
	
def item(request, id_item):
	dato = get_object_or_404(Item, pk=id_item)
	comentarios = Comentario.objects.filter(item=dato)
	return render_to_response('item.html',{'item':dato,'comentarios':comentarios}, context_instance=RequestContext(request))

	