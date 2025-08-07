from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Home Page")

def home(request):
    return render(request, "index.html")   