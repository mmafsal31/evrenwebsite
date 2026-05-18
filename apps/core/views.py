from django.shortcuts import render
from django.views.generic import TemplateView

from .models import SiteSettings, HeroSlide, Statistic, InstitutionProfile, TeamMember
from apps.courses.models import Course
from apps.branches.models import Branch
from apps.facilities.models import Facility


def get_site_settings():
    """
    Returns the existing SiteSettings object.
    Creates one automatically if none exists.
    """
    return SiteSettings.objects.first() or SiteSettings.objects.create()


def get_institution_profile():
    return InstitutionProfile.objects.first() or InstitutionProfile.objects.create()


class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Global site settings
        context['site_settings'] = get_site_settings()

        # Active hero slides only
        context['hero_slides'] = HeroSlide.objects.filter(
            is_active=True
        ).order_by('order')

        # Statistics section
        context['statistics'] = Statistic.objects.all().order_by('order')

        # Leadership team (show first 6)
        context['team_members'] = TeamMember.objects.all().order_by('order')[:6]
        context['institution_profile'] = get_institution_profile()
        context['branches'] = Branch.objects.filter(is_active=True).order_by('order')[:2]
        context['facilities'] = Facility.objects.all().order_by('order')[:6]

        # Featured courses for homepage
        # If your Course model has is_active field, filter by it.
        try:
            context['courses'] = Course.objects.filter(
                is_active=True
            ).order_by('-id')[:6]
        except Exception:
            # Fallback if is_active field does not exist
            context['courses'] = Course.objects.all().order_by('-id')[:6]

        # Optional featured courses alias
        context['featured_courses'] = context['courses']

        return context


class AboutPageView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institution_profile'] = get_institution_profile()
        context['statistics'] = Statistic.objects.all().order_by('order')
        return context


class PeoplePageView(TemplateView):
    template_name = 'core/people.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        members = TeamMember.objects.all().order_by('role', 'order')
        context['people_groups'] = {
            'Principal': members.filter(role='principal'),
            'Faculty': members.filter(role='faculty'),
            'Advisory Board': members.filter(role='advisory_board'),
            'Associates': members.filter(role='associate'),
        }
        return context


def page_not_found(request, exception=None):
    """
    Custom 404 page.
    """
    return render(
        request,
        'errors/404.html',
        {
            'site_settings': get_site_settings(),
        },
        status=404
    )


def server_error(request):
    """
    Custom 500 page.
    """
    return render(
        request,
        'errors/500.html',
        {
            'site_settings': get_site_settings(),
        },
        status=500
    )
