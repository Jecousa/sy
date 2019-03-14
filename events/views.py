from django.shortcuts import render

def index(request):
    return render(request, 'events/events.html')

def event(request):
    return render(request, 'events/event.html')