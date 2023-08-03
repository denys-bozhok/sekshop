from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('',  views.ReviewList.as_view()),
    path('get_review/', views.ReviewView.as_view()),
    path('thank-you', views.ThankYouView.as_view()),
    path('<int:pk>/', views.ReviewSingleView.as_view()),
]
