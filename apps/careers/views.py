from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import messages

from .models import JobOpening, JobApplication
from apps.core.models import InstitutionProfile

class CareersView(ListView):
    model = JobOpening
    template_name = "careers/careers.html"
    context_object_name = "jobs"
    queryset = JobOpening.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["institution_profile"] = InstitutionProfile.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        job_id = request.POST.get("job")
        job = JobOpening.objects.filter(id=job_id, is_active=True).first()
        resume = request.FILES.get("resume")

        if not job or not resume:
            messages.error(request, "Please select a job opening and upload your resume.")
            return redirect(request.path)

        JobApplication.objects.create(
            job=job,
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            resume=resume,
            cover_letter=request.POST.get("cover_letter", "").strip(),
        )
        messages.success(request, "Your career application has been submitted successfully.")
        return redirect(request.path)
