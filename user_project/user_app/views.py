from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    print(request)
    print("You have landed on the home page")
    context = {
        'all_users': User.objects.all(),
        'all_messages': Message.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    print("The user submitted a form!")
    print(request.POST)
    print(request.POST['email'])
    new_user = User.objects.create(email=request.POST['email'], password=request.POST['password'])
    print(new_user)
    return redirect('/')

def mess(request):
    # post/create message
    mess = Message.objects.create(message=request.POST['message'], poster=User.objects.filter(email=request.POST['email']))
    print(mess)
    return redirect('/')


# Create your views here.
