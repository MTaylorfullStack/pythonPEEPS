from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

## Rendering Views

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'wall_messages': Wall_Message.objects.all()
    }
    return render(request, 'success.html', context)
## Logging in and registering

def register(request):
    print(request.POST)
    # Create a user object
    if request.POST['pw'] != request.POST['confpw']:
        return redirect('/')
    else:
        errors = User.objects.basic_validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/success')

def login(request):
    print(request.POST)
    # retrieving a user from the db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')

def post_mess(request):
    Wall_Message.objects.create(message=request.POST['mess'], poster=User.objects.get(id=request.session['id']))
    return redirect('/success')