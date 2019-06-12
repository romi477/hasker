from django.urls import path
from .views import *


urlpatterns = [
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogOutFormView.as_view(), name='logout'),
    path('profile/', person_profile, name='person_profile'),
    path('profile/update/', UpdateProfile.as_view(), name='update_profile'),
    path('<nick>/', person_info, name='person_info'),
]
