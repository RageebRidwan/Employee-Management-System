from django.shortcuts import render
from user.models import Profile


def entry(request):
    return render(request, "entry.html")


def home(request):
    data = Profile.objects.all()
    return render(request, "home.html", {"data": data})
