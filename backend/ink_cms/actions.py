from django.http import Http404, JsonResponse

from ink_cms.history import (
    clone_revision,
    create_revision,
    publish_revision,
    unpublish_object,
)
from ink_cms.models import Revision, Tag


def handle_save(change, data, form, request):

    # Create and validate form and JSON response
    if not form.is_valid():
        return JsonResponse(form.errors, status=400)

    if change:
        obj = form.instance
    else:
        obj = form.save()
        obj.created_by = request.user
        obj.save()
    create_revision(data, obj, request.user)
    if change:
        return JsonResponse(
            {
                "messages": [{"type": "success", "content": "Save successful"}],
                "id": obj.id,
                "data": data,
            }
        )
    else:
        return JsonResponse({"id": obj.id}, status=201)


def handle_revert(data, object_id, request):
    revision_id = int(data.get("revision_id"))
    try:
        revision = Revision.objects.get(id=revision_id, object_id=object_id)
    except Revision.DoesNotExist:
        raise Http404()
    new_revision = clone_revision(revision)
    return JsonResponse({"success": True, "data": new_revision.data})


def handle_publication(data, form, request):
    if not form.is_valid():
        return JsonResponse({"valid": False, "errors": form.errors}, status=400)

    obj = form.save()
    data["workflowstate"] = "Published"
    obj.tags.clear()
    for tag_name in data.get("tags", []):
        tag, created = Tag.objects.get_or_create(name=tag_name)
        obj.tags.add(tag)
    revision = create_revision(data, obj, request.user, action="Published")
    publish_revision(revision)
    return JsonResponse(
        {
            "valid": True,
            "messages": [{"type": "success", "content": "Publication successful."}],
            "data": data,
            "id": obj.id,
        }
    )


def handle_unpublication(obj):
    unpublish_object(obj)
    return JsonResponse(
        {
            "success": True,
            "messages": [
                {"type": "success", "content": "Content was successfully unpublished"}
            ],
        }
    )
