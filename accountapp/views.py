
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from accountapp.models import HelloWorld
# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('text_input')
        new_hello_world = HelloWorld() # 새로운 객체가 new_hello_world에 저장됨
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # return redirect('/account/hello_world/')
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})