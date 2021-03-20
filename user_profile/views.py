from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_profile.forms import AuthUserForm, RegisterUserForm


class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    # success_url = reverse_lazy('edit_page')
    success_url = "profiles.html"

    # def get_success_url(self):
    #     return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'login.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')
