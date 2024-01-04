from django.db import models


# Create your models here.
class Writer(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='writer_image')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='book_image')
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)

    def __str__(self):
        return str(self.title)


class BookIndex(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    index_title = models.TextField()
    index_no = models.IntegerField()
    file = models.FileField(upload_to='book_index_pdfs')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)

    def __str__(self):
        return str(str(self.book.title) + str(self.index_title))
