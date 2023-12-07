from django.db import models


# Create your models here.
class LookupField(models.Model):
    title = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='lookup_image', null=True, blank=True)
    file = models.FileField(upload_to='lookup_file', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'lookup_field'
