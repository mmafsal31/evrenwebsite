
from django.core.cache import cache
from django.utils import timezone

from .models import Popup, SiteSettings


def site_settings(request):
    try:
        site = cache.get('site_settings')
        if site is None:
            site = SiteSettings.objects.first() or SiteSettings.objects.create()
            cache.set('site_settings', site, 60)
    except Exception:
        site = None

    now = timezone.now()
    popup_queryset = Popup.objects.filter(is_active=True).exclude(end_date__lt=now)
    popup_queryset = popup_queryset.filter(start_date__isnull=True) | popup_queryset.filter(start_date__lte=now)

    if request.path == '/':
        popup_queryset = popup_queryset.filter(show_on_homepage=True)

    popup = popup_queryset.order_by('display_order', '-updated_at').first()

    return {
        'site_settings': site,
        'active_popup': popup,
    }
