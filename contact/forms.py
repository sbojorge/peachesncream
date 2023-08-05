from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form to create a contact
    """
    class Meta:
        model = Contact
        fields = ['reason', 'content']

        labels = {
            'reason': 'Why would you like to contact us?',
            'content': 'Tell us how we can improve your experience',
        }
