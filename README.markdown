# Mental Check\-In

## Installation

For the WebApp to be functional, Djangos must be installed.
To install Djangos, use the following website: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment

Once the Django virtual environment is created, locate the folder where you will find the main script for managing projects, called manage.py.

Once found execute the following command to locally host the webserver:
```bash
$ python3 manage.py runserver
```
If the program was successfully executed, you should see the following message:
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 01, 2022 - 01:19:16
Django version 4.0.2, using settings 'mytestsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Once the server is running you can view the web app by navigating to the following URL on your local web browser: http://localhost:8000/
