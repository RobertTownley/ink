import os

from django.utils import timezone

from ink_cms.config import INK_CONFIG


def get_datestamped_upload_path(obj, filename):
    if INK_CONFIG["FLATTEN_UPLOAD_DIR"]:
        # Don't datestamp upload path, eg "/media/2020/01/01/myfile.jpg"
        return filename
    now = timezone.localtime()
    return os.path.join(str(now.year), str(now.month), str(now.day + 1), filename)
