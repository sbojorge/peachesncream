from django.urls import path
from .views import LandingPage, HomePage


urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('home/', HomePage.as_view(), name='home')
]
