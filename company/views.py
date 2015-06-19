from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Project
# Create your views here.

def home(request):
    return render_to_response('web/company_zh/home.html',{},context_instance=RequestContext(request))

def contact(request):
    return render_to_response('web/company_zh/contact.html',{},context_instance=RequestContext(request))
def portfolio(request):

    projects = Project.objects.all()
    return render_to_response('web/company_zh/portfolio.html',{'projects':projects},context_instance=RequestContext(request))
