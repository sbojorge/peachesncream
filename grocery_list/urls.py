from django.urls import path
from .views import AddList, Index


urlpatterns = [
    path('', AddList.as_view(), name='add_list'),
    path('index/', Index.as_view(), name='index'),
]
