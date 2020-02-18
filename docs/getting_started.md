# Getting Started with Ink

This is a more in-depth walk through for getting an opinionated local development
environment set up for a Django project that uses Ink as a CMS. It does not presume
any prior knowledge of Docker, Django, Ink, or any other tools used. It requires only
familiarity with a command line and file editor.

If you already know how to use Django, you may prefer to set up an environment for
yourself, and then follow the
[installation steps](https://github.com/roberttownley/ink) instead.

This guide was written with Mac or Linux in mind, and tested on a machine running
Ubuntu 18.04. If you encounter any difficulties while following along, please read
through the project's [open issues](https://github.com/RobertTownley/ink/issues)
and file an issue if your issue persists.

## Requirements
The libraries below are recommended for following along with this guide.
For each dependency, run the test command to see if it's working properly.

Docker:
  - Test command: `docker --version`
  - Recommended version: >= 18.00
  - [How to install Docker](https://docs.docker.com/install/)

Docker Compose:
  - Test Command: `docker-compose --version`
  - Recommended Version: >= 1.23.0
  - [How to install Docker Compose](https://docs.docker.com/compose/install/)


## Install

Create a new project folder
```
mkdir -p ~/Projects/mysite
cd ~/Projects/mysite
```

### Setting Up Docker
Docker is a program for running programs within "containers", which allows your
programs to run consistently across different platforms and versions. Docker Compose
is a program that enables you to run multiple containers simultaneously. For this
project, we'll have one container running our django project, and another running
a postgres database. You can add more containers (called "services" in docker-compose)
as needed.

Create a file called `docker-compose.yml` and input the following:
```
version: "3"

services:
  db:
    env_file: ./.env
    image: postgres
    restart: always
    volumes:
      - dbdata:/var/lib/postgresql/data/
  backend:
    build: ./backend
    depends_on:
      - db
    env_file: ./.env
    links:
      - db:db
    ports:
      - "8000:8000"
    restart: always
    stdin_open: true
    tty: true
    volumes:
      - ./backend:/backend

volumes:
  dbdata:
```

Create a sub-folder in which to store the code associated with the backend project:
```
mkdir -p ~/Projects/mysite/backend
cd ~/Projects/mysite/backend
```

Within that folder, create a file called `Dockerfile` containing the following:
```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
EXPOSE 8000
WORKDIR /backend

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

CMD /backend/entrypoint.sh
```

This file tells Docker what steps it should take to create the container that we'll
be using. These specific commands tell Docker to expose port 8000, install poetry (for
dependency management), and run a command called `entrypoint.sh` whenever the
container starts.

The last part of the docker setup is to create a hidden file at the project root
called `.env`. Docker reads from this to set environment variables within the
container. Create this file at the root of your project, and input the following:
```
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=postgres_db
SECRET_KEY=FIXME
```

Note: In production, it's important to change `SECRET_KEY` to something more secure.

### Setting Up Poetry
We'll be using `poetry` for dependcy management within the container, so we need to
set up the files that poetry will need for dependency tracking.

Create an empty file for `poetry.lock`
```
cd ~/Projects/mysite/backend
touch poetry.lock pyproject.toml
```

Edit `pyproject.toml` to contain the following, customizing as-needed:
```
[tool.poetry]
name = "mysite"
version = "0.1.0"
description = "My personal website"
authors = ["ENTER YOUR NAME"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.6"
django = "^3.0.2"
ink-cms = "^0.2.0"
psycopg2 = "^2.8.4"
easy-thumbnails = "^2.7"
djangorestframework = "^3.11.0"

[tool.poetry.dev-dependencies]
django-extensions = "^2.2.6"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

Create a bash script at `backend/entrypoint.sh` and mark it as executable.
This file will serve as the initialization script for your dev environment.
```
cd ~/Projects/mysite/backend
touch entrypoint.sh
chmod +x entrypoint.sh
```

Place the following into `entrypoint.sh`:
```
#!/bin/sh

set -e

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

If all went well, you should be able to build the docker images. Run the following
and confirm that docker reports `Successfully tagged mysite_backend:latest`
```
docker-compose build
```

### Setting Up Django
Create an initial django app within the container:
```
docker-compose run backend django-admin startproject backend .
```

The files generated by Docker will be owned by `root` by default. This is true of
the initial project files, as well as whenever you create migrations through Docker.
Whenever these files are generated, you may want to change ownership to your user:
```
cd ~/Projects/mysite
sudo chown -R ${USER}:${USER} *
```

The Django project is now fully functional, but needs to be configured with Ink
settings. Change directories into `backend` and then open up `backend/settings.py`
(full file path is `~/Projects/mysite/backend/backend/settings.py`) and edit/add
the following values:
```
# Place these values directly after django's internal apps
INSTALLED_APPS = [
    ...
    "easy_thumbnails",
    "ink_cms",
    "rest_framework",
    ...
]

# Database values are read in from docker hostnames and environment variables
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": "db",
    }
}

# Ensure that static and media assets are served up during development and production
MEDIA_ROOT = "MEDIA"
MEDIA_URL = "/media/"
STATIC_ROOT = "STATIC"
STATIC_URL = "/static/"

# Set custom values for frontend templates
INK_CONFIG = {
    "FRONTEND_CONTEXT": {
        "blogAvatar": "/static/ink_cms/assets/sample.jpg",
        "blogSidebarText": "<p>Hi everyone! My name is Foo and I write about programming! Stay tuned for more great content!</p>",
        "blogSubtitle": "",
        "blogTitle": "My Customized Blog Title",

    }
}
```

Django Ink has a few values that need to be present within `urls.py` for it to work
properly. Add these values (with or without blog views) to `backend/urls.py`:
```
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ink_cms.views import BlogEntryDetailView, BlogEntryListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ink/", include("ink_cms.urls")),
    path("blog/", BlogEntryListView.as_view()),
    path("blog/<slug:slug>/", BlogEntryDetailView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

If you start up your local containers, you should now be able to see the Django
project running in your web browser. Run `docker-compose up` and visit
`http://localhost:8000/admin/` and confirm that you're presented with a login page.

With the container still running in another window, create a superuser that will enable
you to log in. Run the following command, and fill in the associated prompts:
```
docker-compose exec backend python manage.py createsuperuser
```

### You're Done!
Log in, and you should see the interface for creating new articles, blog entries,
and pages. If you visit `http://localhost:8000/blog/` you can see all blog entries
that you've published so far. You can also access any data programatically through
the API at `http://localhost:8000/ink/api/v1/`.

Refer to the [config documentation](configuration.md) for more info on how you can
customize your blog instance.
