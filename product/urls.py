from django.urls import path
from .views import RankingView, ProductView, ProductDetailView


urlpatterns = [
    path('/rank', RankingView.as_view()),
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view())
]