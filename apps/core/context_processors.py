
from .models import SiteSettings

def site_settings(request):
    try:
        site = SiteSettings.objects.first() or SiteSettings.objects.create()
    except:
        site = None
    return {'site_settings': site}
