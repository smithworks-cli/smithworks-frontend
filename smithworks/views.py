from django.shortcuts import render

# Create your views here.


def dashboard(request):
    context = {"page_name": "Dashboard"}
    return render(request, "dashboard.html", context)


def profile(request):
    context = {"page_name": "Profile"}
    return render(request, "profile.html", context)
