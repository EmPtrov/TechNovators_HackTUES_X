from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello! If you want to use Buddy for Study type /polls/math (for Math AI); /polls/ip (for IP calculating AI); polls/genera l(for General AI)")

def math_AI(request):
    myvariable = "You are using Math AI"
    context={'myvariable' : myvariable}
    return render(request, "base.html", context)
def IP_AI(request):
    ipvar = 'Something'
    context1={'ipvar': ipvar}
    return render(request, "ip.html", context1)
def general_AI(request):
    genvar = 'Hi'
    context2 = {'genvar': genvar}
    return render(request, "gen.html", context2)
