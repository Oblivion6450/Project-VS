from django.urls import path
from users import views as userViews
from django.contrib.auth import views as authViews
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login

app_name = 'users'

urlpatterns = [
    path('registration/', userViews.register, name="reg"),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name='shop/product/list.html'), name="exit"),

]