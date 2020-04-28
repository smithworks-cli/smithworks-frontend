"""list_scrubber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from account.views import registration_view
from smithworks.views import dashboard, profile, save_profile

# Smithworks URLs
urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("save_profile/", save_profile, name="save_profile"),
]

# Alternate view folders
urlpatterns += [
    path("register/", registration_view, name="register"),
]
