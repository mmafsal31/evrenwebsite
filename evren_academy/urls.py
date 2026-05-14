
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('courses/', include('apps.courses.urls', namespace='courses')),
    path('branches/', include('apps.branches.urls', namespace='branches')),
    path('facilities/', include('apps.facilities.urls', namespace='facilities')),
    path('gallery/', include('apps.gallery.urls', namespace='gallery')),
    path('testimonials/', include('apps.testimonials.urls', namespace='testimonials')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admissions/', include('apps.admissions.urls', namespace='admissions')),
    path('contact/', include('apps.contact.urls', namespace='contact')),
    path('careers/', include('apps.careers.urls', namespace='careers')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots, name='robots'),
    path('privacy-policy/', TemplateView.as_view(template_name='pages/privacy_policy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.server_error'
