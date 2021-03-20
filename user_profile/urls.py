from django.urls import path

from user_profile import views
urlpatterns = [
    path('login/', views.MyprojectLoginView.as_view(), name="login"),
    path('register/', views.RegisterUserView.as_view(), name="register"),
    path('logout',views.MyProjectLogout.as_view(), name="logout"),
]