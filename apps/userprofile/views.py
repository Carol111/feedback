from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'userprofile/register.html', {'form': form})

@login_required
def settings(request):
    return render(request, 'userprofile/settings.html')
