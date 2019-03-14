from django.shortcuts import render
from django.http  import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
    
def blog(request):
    return render(request, 'pages/blog.html')

def events(request):
    return render(request, 'pages/events.html')

def services(request):
    return render(request, 'pages/services.html')