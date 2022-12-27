# Intobi restaurant app

Internal service for employees which gives opportunity for them to make a decision about menu on lunch place.


[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Documentation

U can find documentation by visiting http://0.0.0.0:8000/api/docs/#/ after deploy

For authentication, we need to use /auth-token/ endpoint

If u using /api/vote/ u need to declare version of front app using Header

Accept: application/json; version=1.0

## Deployment

The following details how to deploy this application.

### Docker

After u clone this repo u need to set up .env variables. Then u can simply run:

        $ docker-compose -f local.yml build

And


        $ docker-compose -f local.yml up -d

### Setting Up Your Users

- To create a **superuser account**
  - Simply move inside backend's container bash shell:

            $ docker exec -it intobi_app_local_django bash

Then use this command:

            $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy intobi_app

Also don't forget to run pre-commit before commit:

    $ pre-commit


#### Running tests with pytest

    $ pytest


### Celery

This app comes with Celery.

To run a celery worker:
 - Simply move inside backend's container bash shell:

            $ docker exec -it intobi_app_local_django bash

``` bash
cd intobi_app
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.
