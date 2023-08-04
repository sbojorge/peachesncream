from django.views import generic


class LandingPage(generic.TemplateView):
    template_name = 'home/landing_page.html'


class HomePage(generic.TemplateView):
    template_name = 'home/home_page.html'
