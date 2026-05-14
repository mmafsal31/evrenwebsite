from django.shortcuts import render
from django.views.generic import TemplateView

class AdmissionPageView(TemplateView):
    template_name = "admissions/admission.html"