# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from veggie411.models import *

def hello(request):
    return HttpResponse("hi")

def home(request):
    return render(request, 'veggie411/home.html', EmailForm())

def submitemail(request):
    if request.method == 'POST':
	form = EmailForm(request.POST)
	if form.is_valid():
	    form.save()
	else:
	    form = EmailForm()

	return render(request, 'veggie411/home.html', {
	    'form':form,
	})
