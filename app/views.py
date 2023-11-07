from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Swayam(request):
    return HttpResponse("<h1><marquee>Hello Swayam</h1></marquee>")

def Abinash(request):
    return HttpResponse("<h1><marquee>Hello Abinash</h1></marquee")