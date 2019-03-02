from django.contrib.auth.models import User
from django.db import models


class ChatBots(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return '{}'.format(self.user.username)

    class Meta:
        verbose_name = 'Chat Bots'
        verbose_name_plural = 'Chat Bots'
