from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.contrib import messages


def index(request):
    form = messageForm()
    user = request.user
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'Thankyou for your message.')
    context = {
        'form':form,
        'user':user
    }
    return render(request,'main.htm',context)

def ludis(request):
    form = messageForm()
    user = request.user
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'Thankyou for your message.')
    context = {
        'form':form,
        'user':user
    }
    return render(request,'ludis.htm',context)