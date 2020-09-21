from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from djangofscratch.books.models import Book

def home(request):
    return render(None, 'index.html', data)

def books(request):
    books = Book.objects.all()
    data = {
        'books_object' : books
    }
    q = request.META.get('q', "")
    errors = []
    if(q == ''):
        errors.append('Enter a search term')
    elif q.len > 20:
        errors.append('Your search term has to be less than 20 characters')
    return render(None, 'books.html', data)
