from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('ranks/', RankList.as_view()),
    path('ranks/<int:pk>/', RankDetail.as_view()),
]