from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

def home(request):
    return render(None, 'index.html', data)

def books(request):
    return render(None, 'index.html')
