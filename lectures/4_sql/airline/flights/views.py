from django.shortcuts import render

from .models import Flight


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    try:
        flight_instance = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        flight_instance = None

    return render(request, "flights/flight.html", {
        "flight": flight_instance
    })
