# apps/contact/views.py

from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages

from .models import ContactMessage
from apps.core.models import SiteSettings


def get_site_settings():
    return SiteSettings.objects.first()


class ContactPageView(TemplateView):
    template_name = "contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_settings"] = get_site_settings()
        return context

    def post(self, request, *args, **kwargs):
        # Save contact message
        ContactMessage.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            message=request.POST.get("message", "").strip(),
        )

        # Show success message
        messages.success(
            request,
            "Thank you! Your message has been submitted successfully."
        )

        # Redirect back to the same page
        return redirect(request.path)