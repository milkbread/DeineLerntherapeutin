from django.shortcuts import redirect, render
from .forms import ContactForm


def home(request):
    return render(request, 'core/home.html')

def impressum(request):
    if request.method == 'GET':
        print((request.GET['t']))
        return render(request, 'core/%s.html' % request.GET['t'])

def json_contact(request):
    if request.method == 'POST':
        return ContactForm(data=request.POST).send()
          
