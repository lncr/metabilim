from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:pk>/', EventDetailView.as_view()),
    path('create/', EventCreateView.as_view()),
    path('list/',EventListView.as_view())
]
