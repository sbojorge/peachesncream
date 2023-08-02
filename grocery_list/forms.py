from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Grocery


class GroceryForm(forms.ModelForm):
    """
    Form to create a grocery shopping list
    """
    class Meta:
        model = Grocery
        fields = ['name', 'shop','item']

        item = forms.CharField(widget=RichTextWidget())

        labels = {
            'name': 'Name of the list',
            'item': 'Add here the items you need to buy',
        }
