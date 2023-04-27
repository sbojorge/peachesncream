from django.urls import path
from .views import AddList


urlpatterns = [
    path('add/', AddList.as_view(), name='add_list'),
]
