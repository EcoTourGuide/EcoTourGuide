# EcoTourGuideApp/views.py

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('EcoTourGuideApp/index.html')
