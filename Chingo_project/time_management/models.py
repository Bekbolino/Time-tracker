from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

    class Meta:
        verbose_name_plural = "Пользователи"

class History(models.Model):
    date = models.CharField(max_length=30, null=True)
    start = models.CharField(max_length=30, null=True)
    end = models.CharField(max_length=30, null=True)
    amount = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_history")

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "start": self.start,
            "end": self.end,
            "amount": self.amount,

        }

    def __str__(self):
        return f"{self.user}            {self.date}"

    class Meta:
        verbose_name_plural = "История"

class Light(models.Model):
    light = models.BooleanField(default=False)