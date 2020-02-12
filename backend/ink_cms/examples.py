def get_example_frontend_context():

    """Default function for users to override for frontend bio data

    This dictionary populates the frontend template on an individual blog
    page with the blog owner's bio, avatar photo, and any other relevant information.

    Expected to return a dictionary filled with serializable values that will
    be passed to the frontend. By default, no bio info is returned.
    """
    return {
        "blogSidebarAvatar": "/static/ink_cms/assets/sample.jpg",
        "blogSidebarLabel": "About Me",
        "blogSidebarText": (
            "<p>This snippet is passed to the frontend through the "
            '"FRONTEND_CONTEXT" setting within "INK_CONFIG". You can override '
            "what appears here within settings.py.</p><p>Example photo by "
            "Nick Morrison on Unsplash</p>"
        ),
        "blogAvatar": "/static/ink_cms/assets/sample.jpg",
        "blogSubtitle": "",
        "blogTitle": "My Customized Blog Title",
    }
