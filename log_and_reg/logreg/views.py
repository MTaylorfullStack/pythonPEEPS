from django.shortcuts import render, redirect
from .models import User

## Rendering Views

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, 'success.html')
## Logging in and registering

def register(request):
    print(request.POST)
    # Create a user object
    if request.POST['pw'] != request.POST['confpw']:
        return redirect('/')
    else:
        new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
        request.session['user'] = new_user.first_name
        return redirect('/success')

def login(request):
    print(request.POST)
    # retrieving a user from the db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session['user'] = logged_user.first_name
            return redirect('/success')
    return redirect('/')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')