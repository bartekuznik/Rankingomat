from .models import CustomUser, Rank
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_customuser_rank(sender, instance, created, **kwargs):
    if created:
        Rank.objects.create(player = instance)