from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('add/', add),
    path('delete/<int:pk>', delete),
    path('<int:pk>', Details.as_view()),
    path('update/<int:pk>', update)
]
