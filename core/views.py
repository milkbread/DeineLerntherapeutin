from django.shortcuts import redirect, render
from .forms import ContactForm


def home(request):
    return render(request, 'core/home.html')


def json_contact(request):
    if request.method == 'POST':
        return ContactForm(data=request.POST).send()
          
