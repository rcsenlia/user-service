from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=20,blank=True,null=True)
    umur = models.CharField(max_length=20,blank=True,null=True)

@receiver(post_save, sender=User)
def create_user_role(instance, created, **kwargs):
    """Create user profile if user object was just created."""
    if created:
        Profile.objects.create(user=instance)
