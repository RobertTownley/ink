from django.utils.text import slugify


def parse_revision_data(data):
    """Provide server-side validation and sanitization of frontend data"""
    # Ensure that the slug is slugified
    data["slug"] = slugify(data.get("slug", "") or data.get("title", ""))
    return data
