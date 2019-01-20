from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('Hello World')
    return render(request, 'index.html')

def frame(request):
    #return HttpResponse('Hello World')
    return render(request, 'frame.html')

def videoplayer(request):
    return render(request, 'videoplayer.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def channel(request):
	return render(request, 'channel.html')

def favoritecreators(request):
	return render(request, 'favoritecreators.html')

def recentvideos(request):
	return render(request, 'recentvideos.html')

