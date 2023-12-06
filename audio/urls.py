from django.urls import path
from . import views

urlpatterns = [
    path('', views.audio_list, name='audio_list'),
    path('audio_folder_files/<int:folder_id>/', views.audio_folder_files, name='audio_list'),
]
