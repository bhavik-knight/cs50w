from django.shortcuts import render

from .models import Flight


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight_instance, passengers = None, None
    try:
        flight_instance = Flight.objects.get(id=flight_id)
        passengers = flight_instance.passengers.all()
    except Flight.DoesNotExist:
        flight_instance = None
    except AttributeError:
        passengers = None

    return render(request, "flights/flight.html", {
        "flight": flight_instance,
        "passengers": passengers
    })
