from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

def hello(request):
    return HttpResponse("Hello world")

def datetime_dynamic(request):
    now = datetime.datetime.now()
    html = "<html><body>%s</body></html>" % now
    return HttpResponse(html)

def add_hours(request, add):
    try:
        add = int(add)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    now_added = now + datetime.timedelta(add)
    return render(None, 'current_datetime.html', {'now': now, 'now_added':now_added, 'add':add})

