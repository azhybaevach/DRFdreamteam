from django.urls import path
from .views import *


urlpatterns = [
    path('post/list', PostListView.as_view()),
]
