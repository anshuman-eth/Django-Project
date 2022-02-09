#I have created this file-Anshuman
from django.http import HttpResponse 
from django.shortcuts import render
def index(request):
    # return HttpResponse("Home")
    dict={"name":"Ansh", "place":"Ghaziabad"}
    return render(request,'index.html', dict)

def removepunc(request):
    return HttpResponse("Remove punc")

def capfirst(request):
    return HttpResponse("Capitalize first")


def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove(request):
    return HttpResponse("Space remove")


def charcount(request):
    return HttpResponse("Char count")