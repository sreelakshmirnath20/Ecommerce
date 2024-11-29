from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView,CreateView
from django.urls import reverse_lazy


# Create your views here.

# class LandingView(View):
#     def get(self,request):
#         return render(request,"landing.html")

class LandingView(TemplateView):
    template_name="landing.html"



# class LoginView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,"login.html",{"form":form})
#     def post(sel,request):
#         form=LoginForm(data=request.POST)
#         if form.is_valid():
#             uname=form.cleaned_data.get("username")
#             pswd=form.cleaned_data.get('password')
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 return redirect("home")
#             else:
#                 messages.error(request,"Login Failed failed!!")
#                 return redirect('log')
#         return render(request,"login.html",{"form":form})


class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(sel,request):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"Login Failed failed!!")
                return redirect('log')
        return render(request,"login.html",{"form":form})




    
# class RegView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         formdata=RegForm(data=request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             messages.success(request,"Registration Successfull!!")
#             return redirect('log')
#         messages.error(request,"Registration failed!!")
#         return render(request,"reg.html",{"form":formdata})


class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy('log')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('landing')
    
