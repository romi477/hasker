from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index_view'),
    path('test/', test, name='test_view'),
    path('tags/', TagListView.as_view(), name='tags_view'),
    path('addquestion/', QuestionCreate.as_view(), name='add_question'),
]