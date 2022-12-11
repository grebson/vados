from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            messages.success(request, _('You have been logged in.'))
            return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

        messages.success(request, _('You have been logged out.'))
        return redirect('home')

    return redirect('home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, _('You have been registered.'))
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)
