import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import DictUser, User

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_dict_user(sender, instance: User, created, **kwargs):
    logger.warning('In stage of creation')
    if created and instance.user_type == 'dict_user':
        DictUser.objects.create(user=instance)
