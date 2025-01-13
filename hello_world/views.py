from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse("you must of POSTed to this page")
    else:
        return HttpResponse(request.method)