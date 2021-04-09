from django.urls import path

from user_profile import views
urlpatterns = [
    path(r'^login/$', views.user_login, name="login"),
    path(r'^register/$', views.register, name="register"),
    path('logout', views.MyProjectLogout.as_view(), name="logout"),
]