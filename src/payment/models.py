import datetime

from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active_until = models.DateTimeField(null=True)

    def get_package(self):
        return self.package.capitalize()

    def get_updated_at(self):
        return self.updated_at

    def is_active(self) -> bool:
        return self.active_until is not None and self.active_until.timestamp() > datetime.datetime.now().timestamp()


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
