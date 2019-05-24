from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .utils import get_json_tree


def index(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        return render(request, 'tree/login.html')


def home(request):
    context = {"json_tree": get_json_tree()}
    return render(request, 'tree/index.html', context)


def login_user(request):
    if request.method == 'POST':
        if request.POST['username']:
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
                )
            if user is not None:
                login(request, user)
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


def fetch_json_tree(request):
    if request.user.is_authenticated:
        return HttpResponse(get_json_tree())
    else:
        return render(request, 'tree/login.html')


def generate_public_link(request):
    return HttpResponse(get_json_tree())
