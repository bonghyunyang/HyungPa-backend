from django.urls    import path
from .views         import (
	PostDetailView,
        PostCommentView,
        PostView,
        CommentView,
        PostReviewView,
)
urlpatterns = [
    path('/description/<int:post_id>', PostDetailView.as_view()),
    path('/commentwrite', PostCommentView.as_view()),
    path('/postmain', PostView.as_view()),
    path('/getcomment', CommentView.as_view()),
    path('/review', PostReviewView.as_view()),
]
