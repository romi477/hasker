from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogOutFormView.as_view(), name='logout'),
    path('profile/', login_required(PersonProfile.as_view()), name='person_profile'),
    path('profile/questions/', login_required(PersonQuestions.as_view()), name='person_questions'),
    path('profile/update/', login_required(UpdateProfile.as_view()), name='update_profile'),
    path('<str:nickname>/', login_required(PersonFreeInfo.as_view()), name='person_info'),

]
