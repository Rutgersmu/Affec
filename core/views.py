from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request, 'core/index.html')

def fun(request):
    return render(request, 'core/fun.html')


def query(request):
    pass