from django.urls import path
from demoforms.views import CommentFormView

urlpatterns = [
    path("comment", CommentFormView.as_view(), name="comment"),
]
