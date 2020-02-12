from django.utils import timezone

from ink_cms.models import Revision
from ink_cms.parsers import parse_revision_data


def create_revision(data, obj, user, action="Edited"):
    # Exclude some fields from saving to the Revision
    data = parse_revision_data(data)
    revision = Revision.objects.create(obj=obj, data=data, user=user, action=action)
    return revision


def clone_revision(revision):
    revision.pk = None
    revision.action = "Reverted"
    revision.save()
    revision.refresh_from_db()
    return revision


def publish_revision(revision):
    obj = revision.obj
    pub_date = timezone.localtime()
    if revision.data.get("pub_date_str") and revision.data.get("pub_time_str"):
        year, month, day = revision.data["pub_date_str"].split("-")
        hour, minute = revision.data["pub_time_str"].split(":")
        pub_date = pub_date.replace(
            year=int(year),
            month=int(month),
            day=int(day),
            hour=int(hour),
            minute=int(minute),
        )

    obj.publication_date = pub_date
    if not obj.first_publication_date:
        obj.first_publication_date = obj.publication_date
    obj.published_revision = revision
    obj.workflowstate = "Published"
    obj.save()


def unpublish_object(obj):
    obj.workflowstate = "Draft"
    revision = obj.published_revision
    revision.pk = None
    revision.action = "Unpublished"
    revision.data["workflowstate"] = "Draft"
    revision.save()

    obj.published_revision = None
    obj.save()
