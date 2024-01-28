from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path("token/",MyTokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("register/",RegisterView.as_view()),
    path("dashboard/",dahsBoard),
    path("profile/<int:pk>/",ProfileDetail.as_view()),
    path("search/<username>/",SerachUser.as_view()),
    path('',getRoutes),
]
