from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})

def eboard(request):
    form = ContactForm()
    return render(request, 'eboard.html', {'form': form})

def events(request):
    form = ContactForm()
    return render(request, 'events.html', {'form': form})

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            email_message = f'Name: {name}\nSubject: {subject}\nEmail: {email}\nMessage: {message}'

            send_mail(subject, email_message, email, ['migofbostoncollege@gmail.com'])
            return redirect('index')
        else:
            return HttpResponse('Invalid form')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




def lectures(request):
    form = ContactForm()
    return render(request, 'lectures.html', {'form': form})

def resources(request):
    return render(request, 'resources.html')

def workshops(request):
    form = ContactForm()
    return render(request, 'workshops.html', {'form': form})
