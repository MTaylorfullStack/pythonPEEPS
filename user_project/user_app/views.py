from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    print(request)
    print("You have landed on the home page")
    return render(request, "index.html")

# methods to CREATE

def process(request):
    print("The user submitted a form!")
    print(request.POST)
    print(request.POST['email'])
    new_user = User.objects.create(email=request.POST['email'], password=request.POST['password'])
    print(new_user)
    return redirect('/all_users')

def mess(request):
    mess = Message.objects.create(message=request.POST['message'], poster=User.objects.get(email=request.POST['email']))
    print(mess)
    return redirect('/all_mess')

def add_like(request, id):
    liked_mess = Message.objects.get(id=id)
    users_who_liked = User.objects.get(email=request.POST['email'])
    liked_mess.users_who_liked.add(users_who_liked)
    return redirect('/all_mess')

# methods render templates
def one_mess(request, id):
    context = {
        'one_mess': Message.objects.get(id=id)
    }
    return render(request, 'one.html', context)


def show_users(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'users.html', context)

def show_mess(request):
    context = {
        'all_mess': Message.objects.all()
    }
    return render(request, 'message.html', context)