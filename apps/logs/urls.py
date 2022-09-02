from django.urls import path
from apps.logs.views import allActionTypeApiView, specificActiontypeApiView, deleteActionTypeApiView

urlpatterns = [
    path('api-actionType/',allActionTypeApiView),
    path('api-actionType/<int:pk>/<int:idUser>/',specificActiontypeApiView),
    path('api-deleteActionType/<int:pk>/<int:idUser>/',deleteActionTypeApiView),
]