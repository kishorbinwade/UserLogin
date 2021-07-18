from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    path('',views.registerPage,name="register"),
    path('signup/',views.SignUp,name="signup"),

]