from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegistrationForm


def home_view(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to a home page or another view
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login page or another view


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to a home page or another view
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})
