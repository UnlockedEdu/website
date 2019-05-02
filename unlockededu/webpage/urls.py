from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions'),
    path('privacy', views.privacy, name='privacy'),
]
