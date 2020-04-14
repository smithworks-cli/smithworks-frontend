from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .forms import ProfileForm
from .models import Profile

# Create your views here.


@login_required()
def dashboard(request):
    context = {"page_name": "Dashboard"}
    return render(request, "dashboard.html", context)


@login_required()
def profile(request):
    context = {"page_name": "Profile"}
    return render(request, "profile.html", context)


@require_GET
@login_required
def get_profile(request, user):
    user_profile = Profile.objects.get(pk=user)
    form = ProfileForm(instance=user_profile)


require_POST
@login_required()
def save_profile(request):
    context = {}
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect
        else:
            return redirect("dashboard")
