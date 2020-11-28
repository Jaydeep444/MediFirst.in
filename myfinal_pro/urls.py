"""myfinal_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myfinal_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.regi, name="register"),
    path('login/', views.log, name="login"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('', views.ind, name="index"),
    path('products/', views.pros, name="products"),
    path('product-details/', views.pro_det, name="product-details"),
    path('cart/', views.cart, name="cart"),
    path('account/', views.account, name="account"),


    path('accounts/', include('allauth.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]