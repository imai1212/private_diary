import logging

from django.urls import reverse_lazy

from django.shortcuts import render
from django.views import generic

from .forms import InquiryForm

logger = logging.getLogger(__name__)



# Create your views here.
class IndexView(generic.TemplateView):
    template_name="diary/index.html"
    
class InquiryView(generic.FormView):
    template_name="diary/Inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inwuiry')

    def form_valid(self, form):
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)