from .views import zito_api
from django.urls import path

urlpatterns = [
    path('api/', zito_api, name="endpoint"),
]
