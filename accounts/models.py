from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='user_avatar/',
        default='user_avatar/default-avatar-icon-of-social-media-user-vector.jpg',
        blank=True,
    )
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username