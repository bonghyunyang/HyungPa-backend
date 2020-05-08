from django.urls import path
from .views import SignInView, SignUpView, HomeView, PostUserView


urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    # path('/user', ReviewUser.as_view()),
    path('/home', HomeView.as_view()),
    path('/<int:user_id>', PostUserView.as_view()),
]