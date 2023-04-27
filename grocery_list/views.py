from django.views.generic.edit import CreateView
from .models import Grocery
from .forms import GroceryForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AddList(LoginRequiredMixin, CreateView):
    """
    Create a grocery shopping list view
    """
    model = Grocery
    template_name = 'grocery_list/add_list.html'
    form_class = GroceryForm
    success_url = '/grocery_list/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddList, self).form_valid(form)
