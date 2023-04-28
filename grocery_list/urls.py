from django.urls import path
from .views import AddList, Index, DisplayItem


urlpatterns = [
    path('', AddList.as_view(), name='add_list'),
    path('index/', Index.as_view(), name='index'),
    path('grocery_list/<int:pk>', DisplayItem.as_view(), name='display_item'),
]
