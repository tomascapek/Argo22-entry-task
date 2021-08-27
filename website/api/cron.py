from .models import ValidationRequest


def process_requests():
    requests = ValidationRequest.objects.filter(status=ValidationRequest.Status.PENDING)

    for request in requests:
        # handle QR code

        request.status = ValidationRequest.Status.VALID
        request.save()
