from django.urls import path, include
from .views import home_view, user_detail_view, transfer_view

urlpatterns = [
    path("", home_view, name="home_view"),
    path("user/<int:id>/<str:name>/", user_detail_view, name="user_detail"),
    path("transfer/", transfer_view, name="transfer_view")
]
