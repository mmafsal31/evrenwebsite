
from django.http import HttpResponse
from django.template.loader import render_to_string

def sitemap(request):
    try:
        xml = render_to_string('sitemap.xml', {}, request=request)
        return HttpResponse(xml, content_type='application/xml')
    except:
        return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>', content_type='application/xml')

def robots(request):
    return HttpResponse('User-agent: *\nDisallow: /admin/\n', content_type='text/plain')
