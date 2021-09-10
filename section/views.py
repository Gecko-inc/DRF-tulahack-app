from django.http import Http404
from django.views.generic import TemplateView

from config.views import common_context
from .models import Section, Article


class Index(TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update(common_context())

        return context


class SectionView(TemplateView):
    section = None

    def get(self, request, *args, **kwargs):
        try:
            self.section = Section.objects.get(slug=kwargs.get("slug"), is_active=True)
        except Section.DoesNotExist:
            raise Http404
        except Section.MultipleObjectsReturned:
            self.section = Section.objects.filter(slug=kwargs.get("slug"), is_active=True).first()

        return super(SectionView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SectionView, self).get_context_data(**kwargs)
        context.update(common_context())
        context['section'] = self.section

        return context
