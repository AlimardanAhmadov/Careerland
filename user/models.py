from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_image = models.ImageField(default='user.jpg', upload_to='site_images')
    current_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.current_user.username