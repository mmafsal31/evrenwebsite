from django.db import models

class SEOPage(models.Model):
    page_name = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=160)
    meta_keywords = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.page_name