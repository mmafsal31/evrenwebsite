
from django.db import models

class AdmissionEnquiry(models.Model):
    name = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=255, blank=True)
    campus_preference = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Admission Enquiries'

    def __str__(self):
        return self.name
