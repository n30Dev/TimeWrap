from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('schedule', schedule),
    path('mindmap', mindmap),
    path('calendar', calendar),
    path('notes', notes),
    path('lists', lists),
    path('dia', dia)
]
