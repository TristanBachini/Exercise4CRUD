from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/',views.create, name="create"),
    path('createbook/',views.createbook, name="createbook"),
    path('deleteauthor/<str:pk>',views.deleteauthor, name="deleteauthor"),
    path('deletebook/<str:pk>',views.deletebook, name="deletebook"),
    path('updateauthor/<str:pk>',views.updateauthor, name="updateauthor"),
    path('updatebook/<str:pk>',views.updatebook, name="updatebook"),
]