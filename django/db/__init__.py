# -*- coding: utf-8 -*-
import random

from django.contrib.auth.management import create_superuser
from django.db.models import signals
from django.contrib.auth import models as auth_models
from django.conf import settings


signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser'
)


def create_admin(app, created_models, verbosity, **kwargs):
    for admin in settings.ADMINS:
        username = admin[0]
        email = admin[1]
        password = random.randrange(0, 10001)
        try:
            auth_models.User.objects.get(username=username)
        except auth_models.User.DoesNotExist:
            print '*' * 80
            print 'Creating admin user -- login: %s, password: %d' % (username, password)
            print '*' * 80
            assert auth_models.User.objects.create_superuser(username, email, password)


signals.post_syncdb.connect(
    create_admin,
    sender=auth_models,
    dispatch_uid='apps.auth.models.create_admin'
)
