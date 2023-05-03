from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Hobi(models.Model):
    hobi = models.CharField(max_length=50,unique=True)

class Genre(models.Model):
    genre = models.CharField(max_length=50,unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,blank=True,null=True,choices=(('P','P'),('L','L')))
    deskripsi =  models.CharField(max_length=150,blank=True,null=True)
    domisili = models.CharField(max_length=150,blank=True,null=True)
    umur = models.IntegerField(blank=True,null=True)
    teman = models.ManyToManyField(User,through="Relationship",symmetrical=False,related_name="teman")
    hobi = models.ManyToManyField(Hobi)
    genre = models.ManyToManyField(Genre)



class Relationship(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_role(instance, created, **kwargs):
    """Create user profile if user object was just created."""
    if created:
        Profile.objects.create(user=instance)
