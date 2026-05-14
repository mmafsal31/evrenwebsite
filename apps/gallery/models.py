
from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
