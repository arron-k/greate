from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(reqeust):
    if reqeust.method == 'POST':
        return render(reqeust, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!'})
    else:
        return render(reqeust, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!'})
