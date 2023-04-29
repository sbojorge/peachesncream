from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Grocery
from .forms import GroceryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class DeleteList(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ 
    Delete a grocery shopping list
    """
    model = Grocery
    template_name = 'grocery_list/grocery_list_confirm_delete.html'
    context_object_name = 'grocery'
    success_url = '/grocery_list/'

    def test_func(self):
        return self.request.user == self.get_object().user


class EditList(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a grocery shopping list
    """
    model = Grocery
    template_name = 'grocery_list/edit_list.html'
    form_class = GroceryForm
    success_url = '/grocery_list/'

    def test_func(self):
        return self.request.user == self.get_object().user


class DisplayItem(UserPassesTestMixin, DetailView):
    """
    Renders the detail of the grocery shopping list
    """
    model = Grocery
    template_name = 'grocery_list/display_item.html'
    context_object_name = 'grocery'

    def test_func(self):
        return self.request.user == self.get_object().user


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
