from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Note

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

def dashboard(request):
    
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        
        new_note = Note.objects.create(
            title = title,
            description = desc
        )
        
        new_note.save()
        return redirect("notes")
    

    
    
    user = request.user
    
    parameters = {
        "user": user
    }
    
    return render(request, "dashboard.html", parameters)

def notes(request):
    
    user = request.user
    notes = Note.objects.all()
    
    parameters = {
        "user": user,
        "notes": notes
    }
    
    return render(request, "notes.html", parameters)