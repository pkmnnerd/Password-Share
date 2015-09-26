from django.shortcuts import render
from django.http import HttpResponse
from .models import Relation
from django.contrib.auth.models import User

def relationships(request):
    str = '['
    for r in Relation.objects.all():
        str += '\n' + r.__str__() + ','
    str = str[0:-1]
    str += ']'
    return HttpResponse(str);

def sharers(request, owner):
    str = '['
    for r in Relation.objects.filter(sharer=owner):
        str += '\n' + r.__str__() + ','
    if str[-1] == ',':
        str = str[0:-1]
    str += '\n]'
    return HttpResponse(str);

def add_user(request):
    user_name = request.POST["name"]
    user_pass = request.POST["name"]
    email = request.POST["email"]
    user = User.objects.create_user(user_name, user_pass, email)
    user.save()
    return HttpResponse("User created.");


# Create your views here.
