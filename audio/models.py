from django.db import models


# Create your models here.
class AudioFolder(models.Model):
    title = models.TextField(null=True)
    image = models.ImageField(upload_to='audio_image')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'audio_folder'


class AudioFolderFiles(models.Model):
    folder = models.ForeignKey(AudioFolder, on_delete=models.CASCADE)
    title = models.TextField(null=True)
    part = models.FloatField(null=True, blank=True)
    file = models.FileField(upload_to='audio_folder_files')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'audio_folder_files'
