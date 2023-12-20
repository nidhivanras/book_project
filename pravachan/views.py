from django.shortcuts import render
from .models import Pravachan, PravachanFolderFiles


# Create your views here.
def pravachan(request):
    pravachan_folder = Pravachan.objects.all()
    context = {
        'pravachan_folder': pravachan_folder,
    }
    return render(request, 'pravachan_list.html', context)


def pravachan_folder_files(request, folder_id):
    folder_files = PravachanFolderFiles.objects.filter(folder_id=folder_id)
    context = {
        'folder_files': folder_files,
    }
    return render(request, 'pravachan_files.html', context)
