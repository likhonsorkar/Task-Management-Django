from django.urls import path
from tasks.views import dashboard, userdash,test
urlpatterns = [
    path('manager-dashboard/', dashboard),
    path('user-dashboard', userdash ),
    path('test', test )
]