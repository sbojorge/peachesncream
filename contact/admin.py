from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    contact = ('user', 'reason', 'created_on', 'updated_on')


admin.site.register(Contact, ContactAdmin)
