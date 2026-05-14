from django.views.generic import ListView, DetailView
from .models import JobOpening

class CareersView(ListView):
    model = JobOpening
    template_name = "careers/careers.html"
    context_object_name = "jobs"
    queryset = JobOpening.objects.filter(is_active=True)