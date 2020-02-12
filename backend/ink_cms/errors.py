from django.http import JsonResponse


def no_revision_found():
    """Revision was deleted or improperly never created.

    Return data so the editor can continue, but inform the user that their data
    may have been lost if something deleted the revision.
    """
    return JsonResponse(
        {
            "messages": [
                {
                    "type": "error",
                    "content": (
                        "Something went wrong, and the latest version "
                        "of this content couldn't be loaded. You may "
                        "continue editing, or contact support for "
                        "further information."
                    ),
                    "persist": True,
                }
            ]
        },
        status=400,
    )
