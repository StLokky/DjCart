# from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from .models import *
# from .forms import NewsForm


def index(request):
    return HttpResponse("Hello, world. You're at the dcart index.")