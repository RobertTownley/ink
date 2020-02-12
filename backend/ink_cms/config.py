from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from ink_cms.examples import get_example_frontend_context


# Defaults for Django Ink
INK_CONFIG = {
    "APP_LABEL": "CMS",
    "FRONTEND_CONTEXT": get_example_frontend_context,
    "CONTENT_MODELS": ["ink_cms.Article", "ink_cms.BlogEntry", "ink_cms.Page"],
    "DEV": False,
    "FLATTEN_UPLOAD_DIR": False,
    "LIST_FIELDS": [
        "authors",
        "lead_block",
        "publication_date",
        "slug",
        "tags",
        "title",
    ],
    "USERNAME_DISPLAY": "__str__",
}
DEFAULT_THUMBNAIL_ALIASES = {
    "": {
        "optimized": {"size": (2600, 1462), "crop": "smart"},
        "thumbnail": {"size": (355, 200), "crop": "smart"},
    }
}

# Incorporating thumbnail settings if they've been set
if getattr(settings, "THUMBNAIL_ALIASES", None):
    INK_CONFIG["THUMBNAIL_ALIASES"] = settings.THUMBNAIL_ALIASES
else:
    INK_CONFIG["THUMBNAIL_ALIASES"] = DEFAULT_THUMBNAIL_ALIASES

# Allowing user preferences to override Ink defaults
if getattr(settings, "INK_CONFIG", None):
    INK_CONFIG.update(settings.INK_CONFIG)

# Populate frontend context data if it's a callable function
if callable(INK_CONFIG.get("FRONTEND_CONTEXT", None)):
    INK_CONFIG["FRONTEND_CONTEXT"] = INK_CONFIG["FRONTEND_CONTEXT"]()


def check_dependencies():
    """Confirm that Ink has been configured properly"""
    required_settings = ["MEDIA_ROOT", "MEDIA_URL", "STATIC_ROOT", "STATIC_URL"]
    for setting in required_settings:
        if not getattr(settings, setting):
            msg = f'Ink configuration issue: "{setting}" missing from settings.'
            raise ImproperlyConfigured(msg)


check_dependencies()
