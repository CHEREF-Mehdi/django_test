from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', userViews.Home.as_view(), name="user-home"),
    path('login/', authViews.LoginView.as_view(template_name='user/login.html'),
         name="user-login"),
    path("logout/", authViews.LogoutView.as_view(), name="user-logout"),
    path('register/', userViews.Register.as_view(), name="user-register"),
]
