from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    class meta:
        fields=['id','title','author','body']
        model=Post