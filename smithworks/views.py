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
    try:
        user_profile = Profile.objects.get(pk=request.user.id)
        profile_form = ProfileForm(instance=user_profile)
    except Profile.DoesNotExist as identifier:
        profile_form = ProfileForm()
    context = {"page_name": "Profile", "profile_form": profile_form}
    return render(request, "profile.html", context)

require_POST
@login_required()
def save_profile(request):
    context = {}
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #TODO Should this redirect to the profile or dashboard
            return redirect("dashboard")
        else:
            return redirect("dashboard")
