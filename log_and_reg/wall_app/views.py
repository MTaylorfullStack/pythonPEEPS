from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'wall_messages': Wall_Message.objects.all()
    }
    return render(request, 'success.html')
