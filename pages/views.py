from django.shortcuts import render
from django.http  import HttpResponse
from events.models import Event
from services.models import Service

def index(request):
    events = Event.objects.order_by('-date').filter(is_published=True)[:3]

    context = {
        'events': events
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
    
def blog(request):
    return render(request, 'pages/blog.html')

def events(request):
    return render(request, 'pages/events.html')

def services(request):
    services = Service.objects.filter(is_published=True)[:3]
    context = {
        'services': services
    }
    return render(request, 'pages/services.html', context)