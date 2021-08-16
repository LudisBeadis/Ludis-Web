from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('ludis/',views.ludis,name='ludis')
]
