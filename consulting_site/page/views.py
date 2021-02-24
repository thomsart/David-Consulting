#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    pass

def mentions_legales(request):
    return render(request, 'mentions_legales.html')
