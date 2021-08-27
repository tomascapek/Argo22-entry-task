from django.db import models


class ValidationRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending"
        EXPIRED = "expired"
        VALID = "valid"
        FRAUD = "fraud"
        ERROR = "error"

    name = models.CharField(
        max_length=128
    )
    surname = models.CharField(
        max_length=128
    )
    data = models.TextField()
    date_sent = models.DateTimeField()
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.PENDING)
