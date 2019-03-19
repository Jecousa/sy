from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Event

def index(request):
    events = Event.objects.order_by('-date').filter(is_published=True)

    paginator = Paginator(events, 3)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)

    context = {
        'events': paged_events
    }
    return render(request, 'events/events.html', context)

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event
    }
    return render(request, 'events/event.html', context)
