from django.shortcuts import render

# Create your views here.
from audio.models import AudioFolder, AudioFolderFiles


def audio_list(request):
    audio_folder = AudioFolder.objects.all()
    context = {
        'audio_folder': audio_folder,
    }
    return render(request, 'pravachan_list.html', context)


def audio_folder_files(request, folder_id):
    folder_files = AudioFolderFiles.objects.filter(folder_id=folder_id)
    context = {
        'folder_files': folder_files,
    }
    return render(request, 'pravachan_files.html', context)
