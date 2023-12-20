from django.db import models


# Create your models here.
class Pravachan(models.Model):
    title = models.TextField(null=True)
    image = models.ImageField(upload_to='pravanchan_image')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pravachan_folder'


class PravachanFolderFiles(models.Model):
    folder = models.ForeignKey(Pravachan, on_delete=models.CASCADE)
    title = models.TextField(null=True)
    part = models.FloatField(null=True, blank=True)
    file = models.FileField(upload_to='pravanchan_folder_files')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pravachan_folder_files'
