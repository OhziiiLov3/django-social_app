from django.shortcuts import render
from .models import Profile

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profiles/profile_list.html",{
        "profiles": profiles
    })

def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "profiles/profile_detail.html",{"profile": profile})

