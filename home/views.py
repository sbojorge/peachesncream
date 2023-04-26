from django.views import generic


class LandingPage(generic.TemplateView):
    template_name = 'home/landing_page.html'
