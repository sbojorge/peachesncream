from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
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


class Index(LoginRequiredMixin, ListView):
    """
    Display the list of created grocery shopping lists
    """
    model = Grocery
    template_name = 'grocery_list/index.html'
    context_object_name = 'grocerys'

    def get_queryset(self, **kwargs):
        grocerys = self.model.objects.filter(user=self.request.user)
        return grocerys
