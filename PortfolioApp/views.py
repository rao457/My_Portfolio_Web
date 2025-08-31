from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ContactForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.
@cache_page(60 * 15)
class HomeView(FormView):
    form_class = ContactForm
    success_url = "/thanks/"   
    template_name = 'home.html'
    def form_valid(self, form):
        form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)
        return super().form_invalid(form)
class ThankView(TemplateView):
    template_name = 'thanks.html'