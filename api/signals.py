from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import DictUser, User


@receiver(post_save, sender=User)
def ensure_dict_user(sender, instance: User, created, **kwargs):
    """Idempotently maintain a DictUser row whenever User.user_type == 'dict_user'.

    Fires on both create and post-create updates, so promoting a user from
    'find_uz_user' → 'dict_user' also provisions the row. Get_or_create avoids
    duplicate-key errors when the row already exists.
    """
    if instance.user_type != 'dict_user':
        return
    DictUser.objects.get_or_create(user=instance)
