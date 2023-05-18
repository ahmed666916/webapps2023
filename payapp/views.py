from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

class MainView(View):
    def get(self, request):
        response = """<html><body><p>Hello World. MainView in HTML<p><body><html>"""
        return HttpResponse(response)


# Create your views here.

def funky(request):
    response = """<html><body><p>This is the funky function sample<p><body><html>"""

    return HttpResponse(response)

def danger(request):
    response = """<html><body><p>Your guess was """+request.GET['guess']+"""<p><body><html>"""
    return HttpResponse(response)

def rest(request, guess):
    response = """<html><body><p>Your guess was """+escape(guess)+"""<p><body><html>"""
    return HttpResponse(response)
