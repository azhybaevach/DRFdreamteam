from django.urls import path
from .views import *


urlpatterns = [
    path('post/list', PostListView.as_view()),
    path('post/create', PostCreateView.as_view()),
    path('post/detail/<int:id>', PostDetailView.as_view()),
    path('categories/list', CategoryListView.as_view()),
    path('categories/create', CategoryCreateView.as_view()),
    path('categories/detail/<int:id>', CategoryDetailView.as_view()),

]
