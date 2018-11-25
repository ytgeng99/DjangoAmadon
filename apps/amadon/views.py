# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'amadon/index.html')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def buy(request, product_id):
    if 'item_count' not in request.session:
        request.session['item_count'] = 0
    if 'total_charge' not in request.session:
        request.session['total_charge'] = 0
    
    if product_id == '1':
        request.session['latest_charge'] = 19.99
    elif product_id == '2':
        request.session['latest_charge'] = 29.99
    elif product_id == '3':
        request.session['latest_charge'] = 4.99
    elif product_id == '4':
        request.session['latest_charge'] = 49.99

    quantity = int(request.POST['quantity'])
    request.session['latest_charge'] *= quantity
    request.session['item_count'] += quantity
    request.session['total_charge'] += request.session['latest_charge']

    return redirect('/amadon/checkout')

def reset(request):
    del request.session['latest_charge']
    del request.session['item_count']
    del request.session['total_charge']
    return redirect('/amadon')