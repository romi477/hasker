from .utils import ErrorMixin
from django.shortcuts import redirect
from django.utils.functional import curry
from django.views.defaults import server_error


def redirect_index(request):
    return redirect('index', permanent=True)


class Custom403(ErrorMixin):
    template = '403.html'
    stat_code = 403


class Custom404(ErrorMixin):
    template = '404.html'
    stat_code = 404


def custom500(request):
    return curry(server_error, template_name='500.html')


