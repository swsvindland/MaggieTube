from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('Hello World')
    return render(request, 'index.html')

def frame(request):
    #return HttpResponse('Hello World')
    return render(request, 'frame.html')

def video_player(request):
    return render(request, 'video_player.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
