from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import datetime

# Create your models here.
class userprofile(models.Model):
    firstName = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    # role = models.TextField(default="lender")
    email = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    check = models.TextField(null=True, blank=True)
    phone = models.TextField(unique=True, null=True, blank=True)
    country = models.TextField(null=True, blank=True)