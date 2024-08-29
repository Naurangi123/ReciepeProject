"""Urls Mapping for User API"""

from django.urls import path
from .views import CreateUserView

app_name='user'

urlpatterns = [
    path('create/', CreateUserView.as_view(),name='create'),
]

