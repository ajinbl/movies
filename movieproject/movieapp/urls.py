from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:id>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
]