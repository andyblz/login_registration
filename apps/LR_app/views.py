# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse, redirect

def index(request):
    
    return render(request,'LR_app/index.html')

# Create your views here.

def register(request):

    return redirect("/register")