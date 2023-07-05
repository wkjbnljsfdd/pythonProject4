
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='main1'),
    path('about/', views.index2, name='about')

]