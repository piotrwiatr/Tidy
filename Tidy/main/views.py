from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "main/index.html", {
        "name": 5
    })

def about(request):
    return HttpResponse("Hello")
