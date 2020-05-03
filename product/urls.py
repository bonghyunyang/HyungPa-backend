from django.urls import include, path
from .views  import ReviewProductView

urlpatterns = [
    path('/product/<int:product_id>', ReviewProductView.as_view())
]
