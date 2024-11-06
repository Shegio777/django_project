from django.shortcuts import render, get_object_or_404, redirect
from event.models import Event
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "event/index.html")


def event(request):
    context = {
        "title": "каталог",
        "events": Event.objects.all(),
    }
    return render(request, "event/event.html", context)

@login_required
def order_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "event/order_details.html", {"event": event})


def card_details(request):
    # Display the card details form
    return render(request, 'event/card_details.html')