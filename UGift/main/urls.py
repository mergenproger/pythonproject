from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.page1),
    path('page_sosal', views.index),
    path('page2', views.page2),
    path('page3', views.page3)

]