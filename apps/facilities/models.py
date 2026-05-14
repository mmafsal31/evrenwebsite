
from django.db import models
from ckeditor.fields import RichTextField

class Facility(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='facilities/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
