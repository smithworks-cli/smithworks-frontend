from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_GET, require_POST
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "email or password is incorrect")

    context = {}
    return render(request, "login.html", context)


def dashboard(request):
    context = {"page_name": "Dashboard"}
    return render(request, "dashboard.html", context)


def profile(request):
    try:
        user_profile = Profile.objects.get(users_id=request.user.id)
        profile_form = ProfileForm(instance=user_profile)
    except Profile.DoesNotExist as identifier:
        profile_form = ProfileForm()
    context = {"page_name": "Profile", "profile_form": profile_form}
    return render(request, "profile.html", context)


def save_profile(request):
    context = {}
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.users = request.user
            profile.save()
            # TODO Should this redirect to the profile or dashboard
            return redirect("dashboard")
        else:
            return redirect("dashboard")
