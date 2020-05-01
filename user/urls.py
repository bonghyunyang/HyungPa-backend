from django.urls    import path
from .views         import (
         PostUserView,
)
urlpatterns = [
    path('/<int:user_id>', PostUserView.as_view()),
]
