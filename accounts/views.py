from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile
from .forms import SignupForm


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

@login_required
def profile(request):
    if request.method == 'GET':
        profile = Profile.objects.get(user=request.user)
        return render(request, 'account/profile.html', {
            'profile': profile,
        })
    else:
        pass


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    else:
        request.POST


@login_required
def user(request):
    return render(request, 'account/user.html')


@login_required
def user_edit(request):
    pass