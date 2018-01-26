# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime

def index(request):
    if not 'display' in request.session:
        request.session['display'] = []
    
    return render(request,'session_words/index.html')

def process(request):
    request.session["word"] = request.POST["word"]
    request.session["color"] = request.POST["color"]
    
    if "font" in request.POST: 
        font = '40px'
    else: 
        font= '16px'

    request.session['font'] = font 

        
    dic = {"word": request.session["word"],
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
            "color": request.session["color"],
            "font": request.session['font']
    }
    temp = request.session['display']
    temp.append(dic)


    
    return redirect('/')

def clear(request):
    request.session['display'] = []
    return redirect('/')


