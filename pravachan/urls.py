from django.urls import path
from . import views

urlpatterns = [
    path('', views.pravachan, name='pravachan'),
    path('pravachan_folder_files/<int:folder_id>/', views.pravachan_folder_files, name='pravachan_list'),
]
