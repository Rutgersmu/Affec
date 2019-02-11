import logging

from django.conf import settings
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {
        'form': form,
    })


def profile(request):
    form = ProfileForm()
    return render(request, 'account/profile.html', {
        'form':form
    })
