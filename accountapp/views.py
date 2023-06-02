from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HellowWorld


# Create your views here.

def hello_world(reqeust):
    if reqeust.method == 'POST':
        temp = reqeust.POST.get('hello_world_input')

        new_hello_world = HellowWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HellowWorld.objects.all()
        return render(reqeust, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
