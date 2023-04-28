from django.urls import path
from .views import AddList


urlpatterns = [
    path('', AddList.as_view(), name='add_list'),
]
