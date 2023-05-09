from django.urls import path
from .views import *

urlpatterns = [
    path('', CommentListView.as_view(), name='home'),
    path('new_comment/<int:parent_id>', NewCommentView.as_view(), name='new_comment'),
]
