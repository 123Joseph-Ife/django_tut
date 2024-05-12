from django.urls import path
from .views import *

app_name = "feed"

urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('details/<int:pk>/', DetailPageView.as_view(), name="detail")
]