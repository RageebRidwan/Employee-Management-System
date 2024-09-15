from django.shortcuts import render, redirect
from .forms import CreateUser, CreateProfile
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created successfully.")
            return redirect("login")
    else:
        form = CreateUser()
    return render(request, "register.html", {"form": form, "type": "Registration"})


def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, "Logged in successfully.")
                login(request, user)

                return redirect("home")
            else:
                messages.warning(
                    request, "You don't have an account. Please register first."
                )
                return redirect("login")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form, "type": "Login"})


@login_required
def user_logout(request):
    logout(request)
    return redirect("entry")


@login_required
def add_profile(request):
    if request.method == "POST":
        form = CreateProfile(request.POST, user=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Your profile has been created.")
            return redirect("home")
    else:
        form = CreateProfile(user=request.user)
    return render(request, "add_profile.html", {"form": form, "type": "Create Profile"})


@login_required
def update_profile(request, pk):
    pass
