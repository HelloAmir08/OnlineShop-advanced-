from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("register")

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')