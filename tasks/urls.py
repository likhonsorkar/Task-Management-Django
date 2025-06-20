from django.urls import path
from tasks.views import showtasks
urlpatterns = [
    path('show-tasks/',showtasks),
]