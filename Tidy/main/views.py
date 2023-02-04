from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .forms import LaptopForm, DesktopForm, CameraForm
# Create your views here.

def index(request):
    return render(request, "main/index.html", {
        "laptopForm": LaptopForm(),
        "desktopForm": DesktopForm(),
        "cameraForm": CameraForm()
    })

def laptopUpload(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name,upload)
            fileUrl = fss.url(file)
            formData = form.cleaned_data
            print(formData)
            return render(request, 'main/result.html', 
            {
                "fileUrl": fileUrl,
            })
    return HttpResponse("bad form")

def desktopUpload(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name,upload)
            fileUrl = fss.url(file)
            formData = form.cleaned_data
            print(formData)
            return render(request, 'main/result.html', 
            {
                "fileUrl": fileUrl,
            })
    return HttpResponse("bad form")

def cameraUpload(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name,upload)
            fileUrl = fss.url(file)
            formData = form.cleaned_data
            print(formData)
            return render(request, 'main/result.html', 
            {
                "fileUrl": fileUrl,
            })
    return HttpResponse("bad form")

def about(request):
    return HttpResponse("Hello")
