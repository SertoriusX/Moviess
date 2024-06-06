from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Additional fields for the user can be added here
  
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)







