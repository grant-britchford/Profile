from django.urls import path, include
from folio import views

urlpatterns = [
    path('', views.index, name='index'),
]