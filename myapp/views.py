from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    
    if request.method == "POST":
        uname = request.POST.get("username")
        pword = request.POST.get("password")
        
        user = auth.authenticate(username = uname, password = pword)
        
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
    
        else:
            return redirect("invalid")
    
    return render(request, "login.html")

def invalid(request):
    return render(request, "invalid.html")