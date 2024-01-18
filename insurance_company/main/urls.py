from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('rates', views.rates, name='rates'),
    path('agents', views.agents, name='agents'),
    path('contacts', views.contacts, name='contacts'),
    path('email', views.email_from_view, name='email'),
]
