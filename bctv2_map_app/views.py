from django.shortcuts import render
from bctv2_map_app.models import Narrative
from django.views import View
from django.views.generic import TemplateView, ListView


def intro_narrative(request):
    welcomepage = Narrative.objects.all()
    return render(request, 'base.html', {'welcomepage': welcomepage})


class ModalView(View):
    def get(self, request, *args, **kwargs):
        welcomepage = Narrative.objects.all()
        return render(request, 'base.html', {'welcomepage': welcomepage})





class ModalTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ModalTemplateView, self).get_context_data(*args, **kwargs)
        welcomepage = Narrative.objects.all()
        # {context: welcomepage}

        return context