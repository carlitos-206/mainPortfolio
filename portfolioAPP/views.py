from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")
def resume(request):
    return render(request, "Resume.html")