from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from accounts.models import Profile, User
from .forms import SignupForm



# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = SignupForm()
#     return render(request, 'account/signup.html', {
#         'form': form,
#     })

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
        pass


def accounts_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("logged in")
        else:
            return HttpResponse("failed")
    else:
        return HttpResponse("failed")


def accounts_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['name']
        nickname = request.POST['nickname']
        user = User.objects.create_user(username=username, password=password, email=email, name=name, nickname=nickname)
        print(user)
        return HttpResponse('user created')
        # except:
        #     return HttpResponse('error')
    else:
        return HttpResponse('error')

