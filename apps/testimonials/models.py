
from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
