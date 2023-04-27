from django.contrib import admin
from .models import Grocery


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_on', 'updated_on')
    list_filter = ('user', 'created_on', 'updated_on')
