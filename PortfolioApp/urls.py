from django.urls import path
from .views import HomeView, ThankView
app_name = 'PortfolioApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thanks/', ThankView.as_view(), name='thanks'),
]