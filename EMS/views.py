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
            Q(name__icontains=query)
            | Q(designation__icontains=query)
        )
        if not data.exists():
            return render(request,'nothing_to_show.html')

    else:
        data = Profile.objects.all()
    return render(request, "home.html", {"data": data})