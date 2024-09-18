from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def eboard(request):
    return render(request, 'eboard.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')

def lectures(request):
    return render(request, 'lectures.html')

def resources(request):
    return render(request, 'resources.html')

def workshops(request):
    return render(request, 'workshops.html')

def error(request):
    return render(request, '404.html')