from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<int:user_id>", views.UsersViewId.as_view())
]
