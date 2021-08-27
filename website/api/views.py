from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ValidationRequest
from .serializers import ValidationRequestSerializer


@api_view(["GET"])
def get_request_status(request, id):
    try:
        validation_request = ValidationRequest.objects.get(pk=id)
    except ValidationRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({"status": validation_request.status}, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_new_request(request):
    serializer = ValidationRequestSerializer(data=request.data)
    if serializer.is_valid():
        created = serializer.save()
        return JsonResponse({"id": created.pk}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
