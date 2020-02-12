import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from ink_cms.config import INK_CONFIG


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        run(*args, **kwargs)


def run(*args, **kwargs):
    if not INK_CONFIG["DEV"]:
        msg = (
            "Refusing to create initial data for Ink outside of development. "
            "This command is for developers working on the Ink library, and "
            "should not be run in production."
        )
        raise Exception(msg)
    user, created = get_user_model().objects.get_or_create(
        username=os.environ["INK_TEST_USER_EMAIL"],
        email=os.environ["INK_TEST_USER_EMAIL"],
        password=os.environ["INK_TEST_USER_PASSWORD"],
    )
    user.is_superuser = True
    user.is_active = True
    user.is_staff = True
    user.set_password(os.environ["INK_TEST_USER_PASSWORD"])
    user.save()
    print(user)
    print(user.username)
    print(user.check_password(os.environ["INK_TEST_USER_PASSWORD"]))
