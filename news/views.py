from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

