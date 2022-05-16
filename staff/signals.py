from django.dispatch import receiver
from django.db.models.signals import post_save

from staff.models import Staff

from PIL import Image


@receiver(post_save, sender=Staff)
def my_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    if instance.image:
        image = Image.open(instance.image.file.file)
        watermark = image.copy()
        watermark = watermark.resize((image.width//5, image.height//5), Image.ANTIALIAS)
        image.paste(watermark, (image.width-image.width//5, image.height-image.height//5))
        image.save(instance.image.path)
        instance.image = instance.image.path
