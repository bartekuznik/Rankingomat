from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('ranks/', RankList.as_view()),
    path('ranks/<int:pk>/', RankDetail.as_view()),
    path('register/', CustomUserRegistration.as_view()),
    path('login/', CustomUserLogin.as_view()),
    path('logout/', CustomUserLogout.as_view()),
    path('update_vip/', UpdateVipStatusView.as_view(), name='update_vip'),
    path('purchase_tokens/', PurchaseTokensView.as_view(), name='purchase_tokens'),
    path('update_tokens/', UpdateTokenView.as_view(), name='update_tokens'),
]