from django.urls import path
from .views import AddList, Index, DisplayItem, EditList, DeleteList


urlpatterns = [
    path('', AddList.as_view(), name='add_list'),
    path('index/', Index.as_view(), name='index'),
    path('grocery_list/<int:pk>', DisplayItem.as_view(), name='display_item'),
    path('edit/<int:pk>', EditList.as_view(), name='edit_list'),
    path('delete/<int:pk>', DeleteList.as_view(), name='delete_list'),
]
