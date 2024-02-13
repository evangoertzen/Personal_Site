from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

def resume(request):
    return render(request, 'app1/resume.html')

def about(request):
    return render(request, 'app1/about.html')

def photos(request):
    path = settings.PHOTOS_DIR
    img_list = os.listdir(path)
    context = {"images": img_list,
               "path": settings.PHOTOS_URL}
    return render(request, 'app1/photos.html', context)

def contact(request):
    return render(request, 'app1/contact.html')
