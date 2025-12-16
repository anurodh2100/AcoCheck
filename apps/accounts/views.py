from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import UserRegistrationForm, UserLoginForm


# ---------------------------
# REGISTER
# ---------------------------
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})


# ---------------------------
# LOGIN
# ---------------------------
def login_view(request):

    next_url = request.GET.get("next") or request.POST.get("next") or None

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = form.get_user()
            selected_role = form.cleaned_data.get('role')

            # Validate role match
            if selected_role and user.role != selected_role:
                messages.error(request, "Selected role does not match your account.")
                return render(request, "auth/login.html", {
                    "form": form,
                    "next": next_url
                })

            login(request, user)
            messages.success(request, "Logged in successfully!")

            # Handle redirect
            if next_url:
                return redirect(next_url)

            return redirect('dashboard:home')

    else:
        form = UserLoginForm()

    return render(request, 'auth/login.html', {
        'form': form,
        'next': next_url
    })


# ---------------------------
# LOGOUT
# ---------------------------
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('accounts:login')


# ---------------------------
# PROFILE PAGE
# ---------------------------
@login_required
def profile_view(request):
    return render(request, "auth/profile.html")
        