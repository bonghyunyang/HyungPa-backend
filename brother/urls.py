from django.urls import path,include

urlpatterns = [
    path('reviewdetail', include('review.urls')),
    path('reviewdetail', include('user.urls')),
    path('reviewdetail', include('product.urls'))
]
