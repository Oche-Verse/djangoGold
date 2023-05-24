from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def index(request):
   return render(request, 'index.html')



def forex2(request):
     return render(request, 'forex2.html')   

def forex1(request):
     return render(request, 'forex1.html')


def forexDetail(request):
   return render(request, 'forexDetail.html')



def gedmentor(request):
   return render(request, 'gedmentor.html')

def gedSchool(request):
   return render(request, 'gedSchool.html')


def speakmentor(request):
   return render(request, 'speakmentor.html')   


def stage3(request):
   return render(request, 'stage3.html')   


