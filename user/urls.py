from django.urls import include, path
from .views import SignInView, SignUpView,ReviewUser


urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/user', ReviewUser.as_view())
]