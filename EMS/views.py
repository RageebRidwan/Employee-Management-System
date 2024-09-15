from django.shortcuts import render
from user.models import Profile
from django.contrib.auth.decorators import login_required


def entry(request):
    return render(request, "entry.html")


@login_required
def home(request):
    data = Profile.objects.all()
    return render(request, "home.html", {"data": data})
