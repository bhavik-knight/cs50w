from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def bhavik(request):
    return HttpResponse("Hello, Bhavik!")


def david(request):
    return HttpResponse("Hello, David!")


def greet(request, name: str):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
