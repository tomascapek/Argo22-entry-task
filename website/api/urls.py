from django.urls import path

from .views import get_request_status, create_new_request


urlpatterns = [
    path("create_request", create_new_request),
    path("status/<int:id>", get_request_status)
]
