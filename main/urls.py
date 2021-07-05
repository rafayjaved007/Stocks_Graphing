from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('test-api', get_data),
    # path('api/', ChartData.as_view()),
    path('second-graph/<int:time>/', SecondGraph.as_view())
]