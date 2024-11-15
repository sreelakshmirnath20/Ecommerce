from django.shortcuts import render
from django.views import View
from .forms import *

# Create your views here.

class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")

class LoginView(View):
    def get(self,request):
        form=LoginForm
        return render(request,"login.html",{"form":form})
