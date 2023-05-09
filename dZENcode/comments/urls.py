from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CommentListView.as_view(), name='home'),
    path('new_comment/<int:parent_id>', NewCommentView.as_view(), name='new_comment'),
]
