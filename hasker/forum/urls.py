from .views import *
from django.urls import path
from hasker.views import Custom403, Custom404, custom500

handler403 = Custom403.as_view()
handler404 = Custom404.as_view()
handler500 = custom500

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('hot-questions/', HotQuestions.as_view(), name='hot_questions'),
    path('tags/<tag_name>/', TagQuestions.as_view(), name='tag_questions'),
    path('add-question/', QuestionCreate.as_view(), name='add_question'),
    path('question/<slug>/', QuestionDetail.as_view(), name='question_detail'),

    path('question/<slug>/like/', like, name='question_like'),
    path('question/<slug>/dislike/', dislike, name='question_dislike'),

    path('question/<slug>/add-reply/', ReplyCreate.as_view(), name='add_reply'),

    path('question/<slug>/<int:reply_pk>/medal/', add_medal, name='add_medal'),
    path('question/<slug>/<int:reply_pk>/like/', like, name='reply_like'),
    path('question/<slug>/<int:reply_pk>/dislike/', dislike, name='reply_dislike')
]




