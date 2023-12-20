from django.db import models


# Create your models here.
class Vichar(models.Model):
    image = models.ImageField(upload_to='vivhar_images')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        db_table = 'su_vichar'
