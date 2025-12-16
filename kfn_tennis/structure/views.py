from django.views.generic import ListView, DetailView
from .models import Subdivision

class StructureHomeView(ListView):
    model = Subdivision
    template_name = 'structure/structure_home.html'
    context_object_name = 'subdivisions'


class SubdivisionDetailView(DetailView):
    model = Subdivision
    template_name = 'structure/subdivision_detail.html'
    context_object_name = 'subdivision'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_members'] = self.object.members.filter(is_active=True)
        return context
