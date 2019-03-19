from django.shortcuts import render, get_object_or_404

from .models import Service

def index(request):
    services = Service.objects.filter(is_published=True)

    context = {
        'services': services
    }
    return render(request, 'services/services.html', context)

def service(request, service_id):
    service= get_object_or_404(Service, pk=service_id)

    context = {
        'service': service
    }
    return render(request, 'services/service.html', context)