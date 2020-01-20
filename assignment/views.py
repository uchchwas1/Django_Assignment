from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render (request, 'index.html')

def signup(request):
    return render (request, 'signup.html')

def timeline(request):
    return render (request, 'timeline.html')

def retrive(request):
    return render (request, 'retrive.html')