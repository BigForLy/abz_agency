from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission, ContentType
from staff.models import Staff
from position_at_work.models import PositionAtWork


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    user = kwargs.get('instance')
    if not user.is_superuser:
        content_type1 = ContentType.objects.get_for_models(
            Staff, PositionAtWork)
        for _, content_type in content_type1.items():
            permissions = Permission.objects.filter(content_type=content_type)
            user.user_permissions.add(*permissions)
