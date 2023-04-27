from django.urls import path
from .views import ShoppingCreateView


urlpatterns = [
    path('', ShoppingCreateView.as_view(), name='create_list')
]
