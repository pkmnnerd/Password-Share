from django.shortcuts import render
from django.http import HttpResponse
from .models import Relation, Uname, Cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import datetime
import urllib


@csrf_exempt
def relationships(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            try:
                owner = request.POST['owner']
                moocher = request.POST['moocher']
                service = request.POST['service']
                if owner == moocher:
                    return HttpResponse(status=400)
                if request.user.username == owner:
                    if User.objects.filter(username=moocher).exists() and not Relation.objects.filter(moocher=moocher).filter(service=service).exists():
                        rel = Relation(sharer=owner, moocher=moocher, service=service)
                        rel.save()
                        return HttpResponse('<script type = "text/javascript">window.location="http://104.131.58.217:8000/manage/"</script>', status=200)
                    else:
                        return HttpResponse(status=400)
                else:
                    return HttpResponse(status=401)
            except KeyError, e:
                return HttpResponse(e)
        else:
            if request.user.is_superuser:
                stri = '['
                for r in Relation.objects.all():
                    stri += '\n' + r.__str__() + ','
                if stri[-1] == ',':
                    stri = stri[0:-1]
                stri += '\n]'
                return HttpResponse(stri);
            else:
                stri = '['
                for r in Relation.objects.filter(sharer=request.user.username):
                    stri += '\n' + r.__str__() + ','
                for r in Relation.objects.filter(moocher=request.user.username):
                    stri += '\n' + r.__str__() + ','
                if stri[-1] == ',':
                    stri = stri[0:-1]
                stri += '\n]'
                print stri
                return HttpResponse(stri);


def sharers(request, owner):
    if request.user.is_authenticated() and request.user.username == owner:
        stri = '['
        for r in Relation.objects.filter(sharer=owner):
            stri += '\n' + r.__str__() + ','
        if stri[-1] == ',':
            stri = stri[0:-1]
        stri += '\n]'
        print stri
        return HttpResponse(stri);
    else:
        return HttpResponse(status=401)

@csrf_exempt
def sharers_with_service(request, owner, service):
    if request.user.is_authenticated():
        if request.method == "DELETE":
            for r in Relation.objects.filter(sharer=request.user.username).filter(service=urllib.unquote(service)).filter(moocher=owner):
                r.delete()
            f = open('api/redirect.html','r')
            text = f.read()
            return HttpResponse(text)
        else:
            stri = '['
            for r in Relation.objects.filter(sharer=owner).filter(service=service):
                stri += '\n' + r.__str__() + ','
            if stri[-1] == ',':
                stri = stri[0:-1]
            stri += '\n]'
            print stri
            return HttpResponse(stri);
    else:
        return HttpResponse(status=401)


def moochers(request, moocher):
    if request.user.is_authenticated() and request.user.username == moocher:
        stri = '['
        for r in Relation.objects.filter(moocher=moocher):
            stri += '\n' + r.__str__() + ','
        if stri[-1] == ',':
            stri = stri[0:-1]
        stri += '\n]'
        print stri
        return HttpResponse(stri);
    else:
        return HttpResponse(status=401)

@csrf_exempt
def moochers_with_service(request, moocher, service):
    if request.user.is_authenticated():
        if request.method == "DELETE":
            for r in Relation.objects.filter(sharer=moocher).filter(service=urllib.unquote(service)).filter(moocher=request.user.username):
                r.delete()
            f = open('api/redirect.html','r')
            text = f.read()
            return HttpResponse(text)
        else:
            stri = '['
            for r in Relation.objects.filter(moocher=moocher).filter(service=service):
                stri += '\n' + r.__str__() + ','
            if stri[-1] == ',':
                stri = stri[0:-1]
            stri += '\n]'
            print stri
            return HttpResponse(stri);
    else:
        return HttpResponse(status=401)


@csrf_exempt
def add_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user(username, '', password)
    user.save()
    f = open('templates/after_register.html', 'r')
    text = f.read()
    return HttpResponse(text)    

@csrf_exempt
def login_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            f = open('api/redirect.html', 'r')
            text = f.read()
            return HttpResponse(text)

        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=401)

@csrf_exempt
def logout_user(request):
    logout(request)
    f = open('templates/to_login.html', 'r')
    text = f.read()
    return HttpResponse(text)



def docs(request):
    f = open('api/docs.html', 'r')
    text = f.read()
    return HttpResponse(text)

@csrf_exempt
def transfer_cookie(request, user, service):
    if request.method == "POST":
        if Cookie.objects.filter(username=request.user.username).filter(moocher=user).filter(service=service).exists():
            Cookie.objects.filter(username=request.user.username).filter(moocher=user).filter(service=service).delete()
        cookie = Cookie(username=request.user.username,moocher=user,service=service,text=request.POST["cookies"])
        cookie.save()
        return HttpResponse("Cookies saved.")
    else:
        for c in Cookie.objects.all():
            if c.username == user and c.service == service and c.moocher == request.user.username:
                return HttpResponse(c.text)
        return HttpResponse(status=404)

def logged_in(request):
    if request.user.is_authenticated():
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)

def current_user(request):
    username = ""
    if request.user.is_authenticated():
        username = request.user.username
    return HttpResponse(username)

# Create your views here.
