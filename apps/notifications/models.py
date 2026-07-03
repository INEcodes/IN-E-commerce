from django.db import models
from apps.common.base_models import UUIDModel, TimeStampedModel
from apps.accounts.models import User

class Notification(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    channel = models.CharField(max_length=20, default="email")