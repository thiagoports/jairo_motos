import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Moto

@receiver(post_delete, sender=Moto)
def delete_moto_image(sender, instance, **kwargs):
    if instance.imagem:
        imagem_path = instance.imagem.path
        if os.path.isfile(imagem_path):
            os.remove(imagem_path)
