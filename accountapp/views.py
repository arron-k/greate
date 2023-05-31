from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(reqeust):
    return render(reqeust, 'accountapp/hello_world.html')
