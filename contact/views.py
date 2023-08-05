from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AddContact(LoginRequiredMixin, CreateView):
    """
    Create a contact form view
    """
    model = Contact
    template_name = 'contact/add_contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddContact, self).form_valid(form)
