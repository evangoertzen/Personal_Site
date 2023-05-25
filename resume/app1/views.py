from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

def resume(request):
    return render(request, 'app1/resume.html')

def vote(request):
    return render(request, 'app1/vote.html')

def photos(request):
    return render(request, 'app1/photos.html')
