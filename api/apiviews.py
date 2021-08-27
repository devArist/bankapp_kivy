from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog.models import *
from api.serializers import *
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.filter(status=True)
        serializers = BlogSerializer(blogs, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def blog(request, pk):
    if request.method == 'GET':
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogSerializer(blog)

        return Response(serializer.data, status=status.HTTP_200_OK)