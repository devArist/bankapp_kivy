from django.shortcuts import render
from django.http import HttpResponse
from api.apiviews import *
# Create your views here.


def index(request):

    return HttpResponse("bonjour")