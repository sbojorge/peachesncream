from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class AddContact(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create a contact form view and add success message into template
    """
    model = Contact
    template_name = 'contact/add_contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    success_message = "contact form was sent successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddContact, self).form_valid(form)
