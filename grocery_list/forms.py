from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Grocery


class GroceryForm(forms.ModelForm):
    """
    Form to create a grocery shopping list
    """
    class Meta:
        model = Grocery
        fields = ['name', 'item']

        item = forms.CharField(widget=RichTextWidget())

        labels = {
            'name': 'Grocery shopping lists name',
            'item': 'Item to purchase'
        }
