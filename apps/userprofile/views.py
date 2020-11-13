from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('list_course')

    return render(request, 'userprofile/register.html', {'form': form})

@login_required
def settings(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()

            return redirect('settings')
    else:
        form = RegisterForm()

    return render(request, 'userprofile/settings.html', {'form': form})
