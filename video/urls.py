from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos_list, name='videos_list'),
]
