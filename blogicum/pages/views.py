from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def csrf_failure(request, reason="", exception=None):
    return HttpResponse(
        render_to_string('pages/403csrf.html'),
        status=403,
    )


def page_not_found(request, exception):
    return HttpResponse(
        render_to_string('pages/404.html'),
        status=404,
    )


def server_error(request):
    return HttpResponse(
        render_to_string('pages/500.html'),
        status=500,
    )
