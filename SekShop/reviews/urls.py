from django.contrib import admin
from django.urls import path

from .views import review, review_list


urlpatterns = [
    path('', review_list, name='review_list'),
    path('get_review/', review, name='review')
]
