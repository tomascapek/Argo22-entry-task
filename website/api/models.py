from django.db import models


class ValidationRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = 1
        EXPIRED = 2
        VALID = 3
        FRAUD = 4

    name = models.CharField(
        max_length=128
    )
    surname = models.CharField(
        max_length=128
    )
    data = models.TextField()
    date_sent = models.DateTimeField()
