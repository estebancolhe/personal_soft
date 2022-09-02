from django.urls import path
from apps.books.views import allBooksApiView, specificBookApiView, deleteBookApiView

urlpatterns = [
    path('api-book/',allBooksApiView),
    path('api-book/<int:pk>/<int:idUser>/',specificBookApiView),
    path('api-deleteBook/<int:pk>/<int:idUser>/',deleteBookApiView),
]