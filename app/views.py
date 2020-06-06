from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint  
from django.core import serializers
from .models import User

# Create your views here.
def home(request):
    # return HttpResponse('Hello from Python!')
    
    users = User.objects.all()
    text = 'hello world'
        
    return render(request, "home.html", 
        {
            'users':users,
            'text':text
        }
    )
    

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
