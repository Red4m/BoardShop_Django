from django.urls import path

from snowboard import views
urlpatterns = [
    path('snowboard/', views.get_home, name="get_home"),
    path('snowboard/<int:pk>/', views.get_one_board, name="get_one_board"),
    path('login',views.get_sign_in_page, name="login"),
]
