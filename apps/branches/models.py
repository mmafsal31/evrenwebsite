
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Branch(models.Model):
    CAMPUS_CHOICES = (
        ('boys', 'Boys Campus'),
        ('girls', 'Girls Campus'),
        ('general', 'General Campus'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    campus_type = models.CharField(max_length=20, choices=CAMPUS_CHOICES, default='general')
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='branches/')
    description = RichTextField()
    infrastructure_details = RichTextField(blank=True)
    facilities_available = RichTextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.city}"
