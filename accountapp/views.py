from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from accountapp.models import HelloWorld
# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('text_input')
        new_hello_world = HelloWorld() # 새로운 객체가 new_hello_world에 저장됨
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'text_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET Method!!!'})