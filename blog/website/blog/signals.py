from datetime import datetime

from django.contrib.auth.models import User, Group
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Author


def request_start_handler(sender, **kwargs):
    print('Request started at', datetime.now())


@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print('Request finished at', datetime.now())


@receiver(post_save, sender=User)
def registered_user(sender, **kwargs):
    user = kwargs.get('instance')
    group = Group.objects.get(name='blog_editor')
    user.groups.add(group)
    print(f'''
    User registered.
    Name: {user}
    Date Time: {datetime.now()}
    ''')


# @receiver(post_save, sender=User)
# def user_save_handler(sender, **kwargs):
#     user = kwargs.get('instance')
#     Author.objects.create(user=user)
#     print(f'''
#     User registered.
#     Name: {user}
#     Date Time: {datetime.now()}
#     ''')
