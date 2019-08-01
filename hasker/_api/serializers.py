from rest_framework import serializers
from questions.models import Question, Reply
from user.models import Person


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['username', 'email']


class QuestionSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'author', 'pub_date']
        
        
class ReplySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ['id', 'related_q', 'body', 'author', 'pub_date']

