from django.shortcuts import render


# global var to have access
tasks = ["foo", "bar", "baz"]


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
