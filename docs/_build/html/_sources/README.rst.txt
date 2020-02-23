


Welcome to My Site documentation!
====================================

This is a simple and basic  **Django User Registration Management with Schedule Events**!!

Django 2.2 and python 3.6

The Functionalities are:

- Project structure
- **HTML5 Templates**
- Template Inheritance
- Functional **tests**


To start using check out the requirements and the quick start guide!

**Requirements**
----------------

- python3 and pip3
- virtualenv
- GNU gettext (to use Internationalization)

Quick Start Guide
-----------------

Project Name

This project is named *User Registration Management with schedule Events*

-mysite - django project name

-virtual environment names: mienv

-mysite/myapp - My App Name

-In mysite/myapp ,install the apps in settings.py

-In mysite set the path for app (myapp)

-In the settings.py add templates_dir in TEMPLATES_DIR[]


Virtual environments and Settings Files
---------------------------------------

First, you must know your Python 3 path:

$ python --version
which is something similar to /usr/local/bin/python3.

Next, create a Development virtual environment with Python 3 installed:

$ mkvirtualenv --python=/usr/local/bin/python3 mienv
where you might need to change it with your python path.

Go to the virtual environment folder with:

$ cd $mienv/bin

Activate virtual environment:

$ source mienv/bin/activate

Tests
-----

We need to update the languages in our Tests to make sure the translation works correclty.

- in **test_internationalization**, update your languages with the translation of title text, here "Welcome to TaskBuster!"
- in **test_localization**, update your languages.
- export DJANGO_SETTINGS_MODULE=mysite.settings
-set PYTHONPATH=pwd
-run the following command,
    python -m django runserver





















