from django.urls import path
from .views  import ReviewDetailView,ReviewCommentView,ReviewView,ReviewReplyView

urlpatterns = [
    path('/description/<int:review_id>', ReviewDetailView.as_view()),
    path('/reviewcomment', ReviewCommentView.as_view()),
    path('/reviewmain', ReviewView.as_view()),
    path('/reviewreply', ReviewReplyView.as_view()),
]