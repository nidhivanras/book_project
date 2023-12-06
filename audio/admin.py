from django.contrib import admin
from .models import AudioFolder, AudioFolderFiles

# Register your models here.

admin.site.register(AudioFolder)
admin.site.register(AudioFolderFiles)
