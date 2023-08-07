from django.views import generic
from grocery_list.models import Grocery


class LandingPage(generic.TemplateView):
    template_name = 'home/landing_page.html'


class HomePage(generic.TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self):
        groceries = Grocery.objects.filter(user=self.request.user)
        context = {'groceries': groceries}
        return context
