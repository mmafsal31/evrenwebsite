from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages

from .models import AdmissionEnquiry
from apps.core.models import InstitutionProfile
from apps.courses.models import Course
from apps.branches.models import Branch

class AdmissionPageView(TemplateView):
    template_name = "admissions/admission.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["institution_profile"] = InstitutionProfile.objects.first()
        context["courses"] = Course.objects.filter(is_published=True).order_by("order", "name")
        context["campuses"] = Branch.objects.filter(is_active=True).order_by("order", "name")
        return context

    def post(self, request, *args, **kwargs):
        AdmissionEnquiry.objects.create(
            name=request.POST.get("name", "").strip(),
            parent_name=request.POST.get("parent_name", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            email=request.POST.get("email", "").strip(),
            course=request.POST.get("course", "").strip(),
            campus_preference=request.POST.get("campus_preference", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        messages.success(request, "Thank you. Your admission enquiry has been submitted successfully.")
        return redirect(request.path)
