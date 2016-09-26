from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method=='GET':
        return HttpResponse('I amb called from GET Request')
    elif request.method=='POST':
        return HttpResponse('I amb called from POST Request')