from .models import Person
from django.apps import apps
from django.views import View
from django.urls import reverse
from django.shortcuts import render
from .forms import PersonForm, PersonProfileForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView, UpdateView


class RegistrationFormView(FormView):
    form_class = PersonForm
    success_url = '/hasker/'
    template_name = 'account/registration.html'

    def form_valid(self, form):
        self.user = form.save()
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)


class UpdateProfile(UpdateView):
    model = Person
    form_class = PersonProfileForm
    template_name = 'account/person_update_form.html'

    def get_object(self, queryset=None):
        person = Person.objects.get(id=self.request.user.id)
        return person
    
    def get_success_url(self):
        return reverse('person_profile')


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'
    success_url = '/hasker/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogOutFormView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class PersonProfile(View):
    
    def get(self, request, *args, **kwargs):
        person = Person.objects.get(id=request.user.id)
        return render(request, 'account/_profile.html', {'person': person})


class PersonQuestions(View):
    
    def get(self, request, *args, **kwargs):
        model = apps.get_model('forum', 'Question')
        questions = model.objects.filter(author__id=request.user.id)
        return render(request, 'account/_questions.html', {'questions': questions})
    

class PersonFreeInfo(View):
    
    def get(self, request, *args, **kwargs):
        nickname = kwargs.get('nickname')
        if request.user.username == nickname:
            return redirect('person_profile')
        person = get_object_or_404(Person, username=nickname)
        return render(request, 'account/_profile.html', {'person': person, 'nickname': nickname})

