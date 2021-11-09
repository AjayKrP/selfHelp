from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    #is_student = models.BooleanField(User, default=True)
    is_mentor = models.BooleanField(User, default=False)

    # other fields here
    def __str__(self):
        return "%s's profile" % self.is_mentor


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)
