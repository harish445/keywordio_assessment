from django.urls import path, include
from . import views

urlpatterns = [
    path('get/', views.getBook),
    path('add/', views.addBook, name='add'),
    path('update/<str:pk>/', views.updateBook, name='update'),
    path('delete/<str:pk>/', views.deleteBook, name="delete"),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]