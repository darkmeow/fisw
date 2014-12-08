from __future__ import unicode_literals
from inventory.models import Administrator, Client
from django.http import HttpResponseRedirect
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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

def isAdmin(u):
	''' Identifies if the user is an administrator.
		Use this with user_passes_test decorator
	'''
	if u.is_authenticated():
		return Administrator.objects.filter( user = u).exists()
	else:
		return False