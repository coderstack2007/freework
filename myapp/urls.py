from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('copy', views.copy),
    path('it/', views.it),
    path('dizayn/', views.dizayn),
    path('', views.index),
    path('index2/', views.index2),
    path('index3/', views.index3),
    path('copy/', views.copy),
    path('action/', views.action),
    path('Sign/', views.Sign),
    path('make/', views.make),
    path('account/', views.account),
    path('register/', views.register),
    path('makeproject/', views.makeproject),
    path('feedback/', views.feedback),
    path('pay/', views.pay),
    path('notfound/', views.notfound),
    path('about/', views.about),
    path('files/', views.files),
    path('customer', views.customer),
    path('experement', views.experement)
]


