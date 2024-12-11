from django.shortcuts import render

# Create your views here.
def welcome(requests, *args, **kwargs):
    return render(requests,"welcome/welcome.html",{})