from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.templatetags.static import static
from django.shortcuts import render_to_response
from inventory.models import Loan
import json


def grafico(request):
    loans = Loan.objects.all().order_by('-loan_date')
    graph = []
    for loan in loans:
    	if loan.return_date != None:
			graph.append({
				'item'			: loan.item.name,
				'client' 		: loan.client.user.first_name + ' ' +loan.client.user.last_name,
				'date'			: loan.loan_date.strftime("%Y-%m-%d %H:%M:%S"),
				'return_date'	: loan.return_date.strftime("%Y-%m-%d %H:%M:%S"),
				'pk'			: loan.id
				}
			)
    	else:
	        graph.append({
				'item'			: loan.item.name,
				'client' 		: loan.client.user.first_name + ' ' +loan.client.user.last_name,
				'date'			: loan.loan_date.strftime("%Y-%m-%d %H:%M:%S"),
				'return_date'	: "",
				'pk'			: loan.id
				}
			)
		
	graphs = json.dumps(graph)
    return render_to_response('testing.csv',{'data': graphs}, context_instance=RequestContext(request))

def grafico_user(request):
    loans = Loan.objects.filter(client__user = request.user)
    graph = []
    for loan in loans:
    	if loan.return_date != None:
			graph.append({
				'item'			: loan.item.name,
				'client' 		: loan.client.user.first_name + ' ' +loan.client.user.last_name,
				'date'			: loan.loan_date.strftime("%Y-%m-%d %H:%M:%S"),
				'return_date'	: loan.return_date.strftime("%Y-%m-%d %H:%M:%S"),
				'pk'			: loan.id
				}
			)
    	else:
	        graph.append({
				'item'			: loan.item.name,
				'client' 		: loan.client.user.first_name + ' ' +loan.client.user.last_name,
				'date'			: loan.loan_date.strftime("%Y-%m-%d %H:%M:%S"),
				'return_date'	: "",
				'pk'			: loan.id
				}
			)
		
	graphs = json.dumps(graph)
    return render_to_response('userdata.csv',{'data': graphs}, context_instance=RequestContext(request))
