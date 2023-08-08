from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Grocery
from .forms import GroceryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class DeleteList(LoginRequiredMixin, UserPassesTestMixin,
                 SuccessMessageMixin, DeleteView):
    """
    Delete a shopping list
    """
    model = Grocery
    template_name = 'grocery_list/grocery_list_confirm_delete.html'
    context_object_name = 'grocery'
    success_url = '/grocery_list/index'
    success_message = "shopping list was deleted successfully"

    def test_func(self):
        return self.request.user == self.get_object().user


class EditList(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin,
               UpdateView):
    """
    Edit a shopping list
    """
    model = Grocery
    template_name = 'grocery_list/edit_list.html'
    form_class = GroceryForm
    success_url = '/grocery_list/index'
    success_message = "shopping list was updated successfully"

    def test_func(self):
        return self.request.user == self.get_object().user


class DisplayItem(UserPassesTestMixin, DetailView):
    """
    Renders the detail of the shopping list
    """
    model = Grocery
    template_name = 'grocery_list/display_item.html'
    context_object_name = 'grocery'

    def test_func(self):
        return self.request.user == self.get_object().user


class Index(LoginRequiredMixin, ListView):
    """
    Display the list of created shopping lists
    """
    model = Grocery
    template_name = 'grocery_list/index.html'
    context_object_name = 'grocerys'

    def get_queryset(self, **kwargs):
        grocerys = self.model.objects.filter(user=self.request.user)
        return grocerys


class AddList(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create a shopping list and add success message into template
    """
    model = Grocery
    template_name = 'grocery_list/add_list.html'
    form_class = GroceryForm
    success_url = '/grocery_list/index'
    success_message = "shopping list was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddList, self).form_valid(form)
