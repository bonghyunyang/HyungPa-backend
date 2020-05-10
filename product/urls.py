from django.urls import path
from .views import ProductView, ProductDetailView, BrandRankingView, NewpickView, ProductRankingView, ReviewProductView


urlpatterns = [
    path('/productrank', ProductRankingView.as_view()),
    path('/brandrank', BrandRankingView.as_view()),
    path('/newpick', NewpickView.as_view()),
    path('', ProductView.as_view()),
    path('/detail/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>', ReviewProductView.as_view())
]