from django.contrib.auth.models import User
from django.db import models

try:
    from cloudinary.models import CloudinaryField
except ImportError:  # pragma: no cover - handled for runtime resilience
    CloudinaryField = models.ImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    tags = models.CharField(max_length=300, blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def tag_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []
