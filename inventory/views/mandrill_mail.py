from django.core.mail import EmailMultiAlternatives
from inventory.models import Administrator, Client, Loan, Project
from django.template import Context
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.templatetags.static import static
import os
from xhtml2pdf import pisa
from django.conf import settings
from django.utils import timezone

def mailbonito(request):

    
    loans = Loan.objects.filter(loan_date__month=timezone.now().month).order_by('-loan_date')
    template_data = {
        'loans':loans, 'STATIC_URL': settings.STATIC_URL
    }
    plaintext_context = Context(autoescape=False)  # HTML escaping not appropriate in plaintext
    subject = render_to_string("mail/message_subject.txt", template_data, plaintext_context)
    text_body = render_to_string("mail/message_body.txt", template_data, plaintext_context)
    html_body = render_to_string("mail/contenido2.html", template_data, context_instance=RequestContext(request))
    
    msg = EmailMultiAlternatives(subject=subject, from_email="sistemainventariowcg@gmail.com",
                                 to=[user.email for user in [project.manager.user for project in Project.objects.all()]], body=text_body)
    msg.attach_alternative(html_body, "text/html")
    html = "<html><body><h1>Hello World</h1><p>Good night!</p></body></html>"
    
    file = open(os.path.join(settings.MEDIA_ROOT, 'email.pdf'), "w+b")
    
    pisaStatus = pisa.CreatePDF(html_body, dest=file,
            link_callback = link_callback)
    
    # Return PDF document through a Django HTTP response
    file.seek(0)
    pdf = file.read()
    file.close()            # Don't forget to close the file handle
    msg.attach('resumen.pdf', pdf , 'application/pdf')
    

    msg.send()
    return HttpResponse(html_body)
    
def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % \
                    (sUrl, mUrl))
    return path