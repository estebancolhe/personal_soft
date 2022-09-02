from django.urls import path
from apps.users.views import registerApiView, loginApiView, logoutApiView, indexApiView


urlpatterns = [
    path('', indexApiView),
    path('api-register/', registerApiView),
    path('api-login/',loginApiView),
    path('api-logout/<int:pk>/',logoutApiView),
]