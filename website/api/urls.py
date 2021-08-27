from django.conf.urls import url

from .views import get_request_status, create_new_request


urlpatterns = [
    url("create_request", create_new_request),
]
