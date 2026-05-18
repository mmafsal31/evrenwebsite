
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from apps.blog.models import BlogPost
from apps.courses.models import Course

def sitemap(request):
    try:
        site_url = getattr(settings, 'SITE_URL', '').rstrip('/') or request.build_absolute_uri('/').rstrip('/')
        xml = render_to_string('sitemap.xml', {
            'site_url': site_url,
            'courses': Course.objects.filter(is_published=True).only('slug', 'created_at'),
            'blog_posts': BlogPost.objects.filter(is_published=True).only('slug', 'updated_at'),
        }, request=request)
        return HttpResponse(xml, content_type='application/xml')
    except Exception:
        return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>', content_type='application/xml')

def robots(request):
    site_url = getattr(settings, 'SITE_URL', '').rstrip('/') or request.build_absolute_uri('/').rstrip('/')
    return HttpResponse(
        f'User-agent: *\nDisallow: /admin/\nSitemap: {site_url}/sitemap.xml\n',
        content_type='text/plain',
    )
