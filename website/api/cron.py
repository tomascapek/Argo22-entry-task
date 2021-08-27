import binascii
import datetime

from PIL import Image
from io import BytesIO
import base64
from pyzbar.pyzbar import decode

from .models import ValidationRequest


def process_requests():
    requests = ValidationRequest.objects.filter(status=ValidationRequest.Status.PENDING)

    for request in requests:
        try:
            image = Image.open(BytesIO(base64.b64decode(request.data)))
        except binascii.Error:
            request.status = ValidationRequest.Status.ERROR
            request.save()
            continue

        data = decode(image)

        try:
            request_date = datetime.datetime.strptime(data[0].data.decode("utf-8"), "%Y-%m-%d").date()
        except ValueError:
            request.status = ValidationRequest.Status.FRAUD
            request.save()
            continue

        if datetime.datetime.now().date() >= request_date:
            request.status = ValidationRequest.Status.EXPIRED
        else:
            request.status = ValidationRequest.Status.VALID
        request.save()
