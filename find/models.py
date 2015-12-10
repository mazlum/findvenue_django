from django.contrib.auth.models import User
from django.db import models
import base64
import hashlib
import random

RANDOM_API_CHOICES = ('rA', 'aZ', 'gQ', 'hH', 'hG', 'aR', 'DD')


class UserKey(models.Model):
    user = models.ForeignKey(User)
    key = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            hashed_value = hashlib.sha256(str(random.getrandbits(256))).digest()
            self.key = base64.b64encode(hashed_value, random.choice(RANDOM_API_CHOICES)).rstrip('==')
        super(UserKey, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.key