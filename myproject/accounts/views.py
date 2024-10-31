from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import logout

def login(request):
    return redirect('social:begin', backend='google-oauth2')

def logout_view(request):
    logout(request)
    return redirect('/')
