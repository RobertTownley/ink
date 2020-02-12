from django.apps import AppConfig

from ink_cms.config import INK_CONFIG


class InkConfig(AppConfig):
    app_name = "ink_cms"
    name = "ink_cms"
    verbose_name = INK_CONFIG["APP_LABEL"]
