# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse, redirect

def register(request):
    
    return render(request,'user_app/register.html')
