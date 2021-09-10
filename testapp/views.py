from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_views(request):
    return HttpResponse('<h1> This is first views')

def second_views(request):
    return HttpResponse('<h1> This is second views')

def third_views(request):
    return HttpResponse('<h1> This is third views')

def fourth_views(request):
    return HttpResponse('<h1> This is fourth views')

def fifth_views(request):
    return HttpResponse('<h1> This is fifth views')
