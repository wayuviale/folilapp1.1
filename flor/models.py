from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
@receiver(post_save, sender=User)    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("Creando perfil para el usuario:", instance.username)
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print("Guardando perfil para el usuario:", instance.username)
    instance.profile.save()