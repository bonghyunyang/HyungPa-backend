from django.urls import include, path
from .views  import ReviewDetailView,ReviewCommentView,ReviewView

urlpatterns = [
    path('/description/<int:review_id>', ReviewDetailView.as_view()),
    path('/comment', ReviewCommentView.as_view()),
    path('/main', ReviewView.as_view())
]
