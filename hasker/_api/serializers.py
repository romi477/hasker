from rest_framework import serializers
from forum.models import Question, Reply
from account.models import Person


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['username', 'email']


class QuestionSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'author', 'pub_date', 'slug']
        
        
class ReplySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ['id', 'related_q', 'body', 'author', 'pub_date']

