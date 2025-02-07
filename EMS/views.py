from django.shortcuts import render
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def entry(request):
    return render(request, "entry.html")



@login_required
def home(request):
    query = request.GET.get("q")
    if query:
        data = Profile.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        )
    else:
        data = Profile.objects.all()
    return render(request, "home.html", {"data": data})