from django.views.generic.base import TemplateView

from .models import Article

class HomePageView(TemplateView):

    template_name = "template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        abc=Article.objects.all().order_by('-id')[:5]
        context['latest_articles'] = reversed(abc)
        return context