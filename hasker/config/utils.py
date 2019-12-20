from django.views import View
from django.shortcuts import render_to_response
from django.template import RequestContext


class ErrorMixin(View):
    template = None
    code = None
    
    def get(self, request, *args, **kwargs):
        context = RequestContext(request)
        response = render_to_response(self.template, context)
        response.status_code = self.code
        return response
    