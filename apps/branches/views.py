
from django.views.generic import ListView, DetailView
from .models import Branch

class BranchListView(ListView):
    model = Branch
    template_name = 'branches/branch_list.html'
    context_object_name = 'branches'

    def get_queryset(self):
        queryset = Branch.objects.filter(is_active=True).order_by('order')
        campus_type = self.kwargs.get('campus_type')
        if campus_type:
            queryset = queryset.filter(campus_type=campus_type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campus_type = self.kwargs.get('campus_type')
        context['page_title'] = {
            'boys': 'Boys Campus',
            'girls': 'Girls Campus',
        }.get(campus_type, 'Our Campus')
        return context

class BranchDetailView(DetailView):
    model = Branch
    template_name = 'branches/branch_detail.html'
    context_object_name = 'branch'
    slug_field = 'slug'
