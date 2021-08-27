from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import ValidationRequestSerializer


@api_view(["POST"])
def create_new_request(request):
    serializer = ValidationRequestSerializer(data=request.data)
    if serializer.is_valid():
        created = serializer.save()
        return JsonResponse({"id": created.pk}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
