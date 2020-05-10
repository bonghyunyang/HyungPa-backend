from django.urls import path,include

urlpatterns = [
    path('product', include('product.urls')),
    path('user', include('user.urls')),
    path('post', include('post.urls')),
    path('review', include('review.urls')),
]
