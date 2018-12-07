from django.urls import path

from . import views

urlpatterns = [
    path('task_completed/<str:course_id>/', views.task_completed),
]
