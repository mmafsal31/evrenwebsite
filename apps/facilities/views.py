from django.views.generic import ListView
from .models import Facility

class FacilityListView(ListView):
    model = Facility
    template_name = "facilities/facility_list.html"
    context_object_name = "facilities"