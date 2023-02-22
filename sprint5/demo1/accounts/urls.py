from django.urls import path
from .views import AccountView, AccountDetailView


urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<int:pk>/", AccountDetailView.as_view()),
]
