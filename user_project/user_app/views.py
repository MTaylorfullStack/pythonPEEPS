from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print(request)
    print("You have landed on the home page")
    return render(request, "index.html")

def process(request):
    print("The user submitted a form!")
    print(request.POST)
    print(request.POST['email'])
    request.session['new_user'] = f"New User Email: {request.POST['email']}, New User PW: {request.POST['password']}"
    return redirect('/')



# Create your views here.
