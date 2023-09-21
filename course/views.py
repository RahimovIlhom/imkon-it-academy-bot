from django.shortcuts import render, redirect


# Create your views here.

def home_view(request):
    return redirect("/admin")