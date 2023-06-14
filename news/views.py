# from django.shortcuts import render
# from rest_framework.status import HTTP_200_OK
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .models import *
from .serializers import PostSerializer
from .serializers import CategorySerializer
from django_filters import rest_framework as filters
from .filters import PostFilter
from rest_framework import filters as fr


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, fr.OrderingFilter)
    ordering_fields = ['id', 'created_date', 'categories']
    filterset_class = PostFilter



class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['title']


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'id'
    serializer_class = CategorySerializer
