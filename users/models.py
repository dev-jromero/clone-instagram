"""Users models."""

#django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biografy = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture= models.ImageField(
        upload_to='users/picture', 
        blank=True, 
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """RETURN username."""
        return self.user.username