from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# AUTENTICAÇÃO -> usuário realmente é quem ele diz ser
urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    # path("login/", views.LoginView.as_view()),
]
