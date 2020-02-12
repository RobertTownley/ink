# Configuration

Configration for Django Ink mostly takes place within `settings.py`. To override default
settings, create a dictionary called `INK_CONFIG` within your `settings.py` file. This
dictionary is referenced at runtime against the default options, with your preferences
overriding defaults.

Below are a list of keys, and their default values:

## Ink Configuration Options

### `APP_LABEL`
Default: `"CMS"`
The value that Ink objects appear under within the Django Admin

### `CONTENT_MODELS`
Default: `["ink_cms.Article", "ink_cms.BlogEntry", "ink_cms.Page"]`

A list containing strings of model names to use as part of the CMS. If this is
overridden with fewer/more models, those models will be activated/deactivated from
the Django Admin.

NOTE: These models will still be made available via the Ink API.

### `DEV`
Default: `False`

When this flag is set to True, templates will use the `django_webpack_loader`
versions of app templates. This is a development utility, and most end users will
not need to set this to `True`.

The dockerized development environment used to develop Ink has this setting
pre-configured. If you'd like to contribute to Django Ink, use of the dockerized
environment is encouraged. For more information, see our
[contribution documentation](contributing.md)

### `FLATTEN_UPLOAD_DIR`
Default: `False`

By default, uploaded images and other content are placed into nested folders
within the app's media directory. This means that assets will have a final path
of `yyyy/mm/dd/example.jpg`. If this is set to `True`, assets will not be placed
into a datestamped path, and instead be available at `example.jpg`. 

### `FRONTEND_CONTEXT`
Default `get_example_frontend_context`

A dict (or callable returning a dict) containing values that should
be passed to frontend templates for rendering.

Default values for this nested dictionary can be found
in [examples.py](../backend/ink_cms/examples.py)

This accepts a dictionary or callable function that returns a dictionary.

NOTE: Values placed into this dictionary will be made accessible to the client,
and should not contain secrets or insecure values.

### `LIST_FIELDS`
Default: `["authors", "lead_block", "publication_date", "slug", "tags", "title"]`

A list of names of fields to return as part of ListView API calls.

This can be useful to override if you're customizing the list page, and want
additional (or less) data returned from the default API serializers.

NOTE: This will not impact the values returned for DetailView. To make more/fewer
fields available to the DetailView of an object, you'll need to override the model
serializer and viewset objects, and expose those through an API endpoint.

### `USERNAME_DISPLAY`
Default: `"__str__"`

The name of the method of the `User` model that should be called to get the
stringified representation of that user.

To override this, give a custom user model a separate method, and pass the name
of that method into the config dict. Alternatively, change the value returned from
your custom user model's `__str__` method.

NOTE: The default Django user model is configured to return `self.username`.

## Other Config Options

## `THUMBNAIL_ALIASES`
Default:
```
"": {
    "optimized": {"size": (2600, 1462), "crop": "smart"},
    "thumbnail": {"size": (355, 200), "crop": "smart"},
}
```
Ink makes use of [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) for
generating optimized crops of images. Configuration settings for easy thumbnails will
be honored if set.

If you choose to override the value of `THUMBNAIL_ALIASES`, ensure that the default
thumbnail aliases include entries called "optimized" and "thumbnail". Both of these
are required by the default serializers.
