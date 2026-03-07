from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

        else:
            return render(request, 'accounts/login.html', {
                "error": "Invalid username and/or password."
            })
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')