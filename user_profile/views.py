from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_profile.forms import AuthUserForm, LoginForm
from .forms import  UserRegistrationForm

# class MyprojectLoginView(LoginView):
#     template_name = 'login1.html'
#     form_class = AuthUserForm
#     # success_url = reverse_lazy('edit_page')
#     success_url = "profiles.html"

    # def get_success_url(self):
    #     return self.success_url


# class RegisterUserView(CreateView):
#     model = User
#     template_name = 'login1.html'
#     form_class = RegisterUserForm
#     success_url = reverse_lazy('edit_page')
#     success_msg = 'Пользователь успешно создан'
#
#     def form_valid(self, form):
#         form_valid = super().form_valid(form)
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         aut_user = authenticate(username=username, password=password)
#         login(self.request, aut_user)
#         return form_valid


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register_page.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')
