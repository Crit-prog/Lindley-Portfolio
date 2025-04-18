from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PrevProj


class HomePageView(TemplateView):
    template_name = 'app/index.html'

def portfolio(request):
    previous_projs = PrevProj.objects.all()
    return render(request, 'app/index.html', {'previous_projs': previous_projs})