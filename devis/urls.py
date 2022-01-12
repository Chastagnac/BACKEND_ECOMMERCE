#Products URL Configuration

from django.urls import path
from devis import views


urlpatterns = [
    path('latest-quote/', views.LatestQuoteList.as_view()),
]