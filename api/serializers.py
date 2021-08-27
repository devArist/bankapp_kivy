from rest_framework import serializers
from blog.models import *

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','date_add', 'title', 'image', 'description')