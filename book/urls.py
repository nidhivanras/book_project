from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_folder_files/<int:folder_id>/', views.book_folder_files, name='book_folder_files_list'),
    path('get_index_pdf/<int:index_id>/', views.get_index_pdf, name='get_index_pdf'),
]
