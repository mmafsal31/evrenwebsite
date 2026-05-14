from django.views.generic import ListView
from .models import GalleryItem

class GalleryListView(ListView):
    model = GalleryItem
    template_name = "gallery/gallery_list.html"
    context_object_name = "items"