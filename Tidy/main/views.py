from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .forms import LaptopForm, DesktopForm, CameraForm
from .gpt import ChatGPT
from time import sleep
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
            return result(request, "laptop", fileUrl, formData)
    return HttpResponse("bad form")

def desktopUpload(request):
    if request.method == "POST":
        form = DesktopForm(request.POST)
        if form.is_valid():
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name,upload)
            fileUrl = fss.url(file)
            formData = form.cleaned_data
            print(formData)
            return result(request, "desktop", fileUrl, formData)
    return HttpResponse("bad form")

def cameraUpload(request):
    if request.method == "POST":
        form = CameraForm(request.POST)
        if form.is_valid():
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name,upload)
            fileUrl = fss.url(file)
            formData = form.cleaned_data
            print(formData)
            return result(request, "camera", fileUrl, formData)
    return HttpResponse("bad form")

def result(request, typeOfProduct, fileUrl="", formData=""):
    inst = ChatGPT()
    # unfortunately had to use aboslute path, couldn't find fix in time
    response = inst.generatePostInfo(typeOfProduct, formData, 'C:/Users/Piotrek/Documents/programming/Tidy/Tidy'+fileUrl)
    return render(request, "main/result.html", {
        "title": response["title"],
        "desc": response["description"],
        "imgs": response["images"]
    })
def about(request):
    return render(request, "main/about.html")
