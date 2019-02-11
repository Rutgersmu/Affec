from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request, 'core/index.html')

def home(request):
    return render(request, 'core/home.html')


def query(request):
    pass