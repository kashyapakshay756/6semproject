from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='home'),
    path("need", views.need, name='need'),
    path("needhome", views.needhome, name='needhome'),
    path("emergency", views.emergency, name='emergency'),
    path("workwithus", views.workwithus, name='workwithus'),
    path("gallery", views.gallery, name='gallery'),
    path("Donate", views.Donate, name='donate'),
    path("work", views.work, name='work'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name="contact"),
    # path("loginuser", views.loginuser, name="loginuser"),
    path("dsblog", views.dsblog, name="dsblog"),
    path("serviseform", views.serviseform, name="serviseform"),
    path("regestation", views.regestation, name="regestation"),
    path("show", views.show, name="show"),
    path("mail", views.mail),
]
