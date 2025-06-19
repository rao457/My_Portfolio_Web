from django.urls import path
from .views import HomeView, ThankView
from django.views.generic import TemplateView
app_name = 'PortfolioApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thanks/', ThankView.as_view(), name='thanks'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", TemplateView.as_view(
        template_name="sitemap.xml",
        content_type="application/xml"
    )),
]