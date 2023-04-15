#from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    s="<h1>****Hello User ,Welcome to Django First  Project (DJMyProject1)&First-App(MyApps1)****</h1><hr/>"
    return HttpResponse(s)
def show(request):
    ss='<center>$$$<h1>Hello User,Welcome to Django FirstProject (DJMyproject) & First-App &GOPI (MyApp1)$$$ </h1></center><hr/>'
    return HttpResponse(ss)

