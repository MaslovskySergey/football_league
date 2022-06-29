from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .forms import SignInForm

'''def registration(request):
    return render(request, 'templates/auth_app/registration.html')'''


class RegistrationView(View):
    """
    # Return home page
    """

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "templates/auth_app/registration.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                login(request, user)
                return redirect('create_commands')

        return render(request, "templates/auth_app/registration.html", context={"form": form})


class SignInView(View):
    """
    # User sign in
    """
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, "templates/auth_app/login.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)

        if form.is_valid():

            user = authenticate(request, **form.cleaned_data)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, "templates/auth_app/login.html", context={"form": form})


