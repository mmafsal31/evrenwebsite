from django.shortcuts import render
from django.views.generic import TemplateView

from .models import CTASection, HeroSlide, InstitutionProfile, SiteSettings, Statistic, TeamMember
from apps.courses.models import Course
from apps.branches.models import Branch
from apps.facilities.models import Facility
from apps.testimonials.models import Testimonial


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
        context['hero_slides'] = HeroSlide.objects.filter(is_active=True).order_by('order')

        # Statistics section
        context['statistics'] = Statistic.objects.all().order_by('order')

        # Homepage leadership section intentionally shows advisory members only.
        context['team_members'] = TeamMember.objects.filter(
            team_category='advisory',
            is_active=True,
        ).order_by('display_order', 'order')[:6]
        context['institution_profile'] = get_institution_profile()
        context['branches'] = Branch.objects.filter(is_active=True).order_by('order')[:2]
        context['facilities'] = Facility.objects.all().order_by('order')[:6]
        context['testimonials'] = Testimonial.objects.filter(is_active=True).order_by('order')[:8]
        context['cta_section'] = CTASection.objects.filter(is_active=True).first()

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
        members = TeamMember.objects.filter(is_active=True).order_by('display_order', 'order')
        context['people_groups'] = {
            'Advisory Board': members.filter(team_category='advisory'),
            'Management Team': members.filter(team_category='management'),
            'Faculty Team': members.filter(team_category='faculty'),
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
