# Offline-Music-DJANGO
# Spotify Clone


This spotify clone is a simple, and private streaming site, with features like adding songs, adding users, admin page, streaming offline, and a few more, and is hosted on localhost __or__ 127.0.0.1. It is fully functional and ready to be deployed with some basic security features against attacks like cross site scripting and SQL injection.
## Features

- Ready to deploy
- Protected against common attacks
- Written in clean code and easily editable
- Comes with common error pages like 404 and 500
- Comes with a development server
- Easy to use admin interface
- Offline streaming
- Adding songs
- etc.

## Technology Used

This Django site uses 2 main technologies, [Python 3.10] and Django 4.1.4 but uses lots of different thing in the background like JavaScript (to stream songs non-stop) and [CSS] (Helps styling the webpages)

## Installation

Install the repository and the following package and you are good to go!
```sh
pip install django==4.1.4
```

To start the development server on 127.0.0.1:8000 __or__ localhost:8000 (for Chrome), run the flowing commands
1. To start the server:

    ```sh
    python manage.py runserver
    ```
    __OR__
    Run the runserver file.
2. To add a user go to 127.0.0.1:8000/signup/ __or__ localhost:8000/signup/
3. To login go to 127.0.0.1:8000/login __or__ localhost:8000/login and login with the credentials you created.
4. Enjoy!

## Admin
The admin username and password are:
* Username: admin
* Password: AdminPassword123

## Development

Want to contribute? Great! Pull requests and issues are welcome! [Here] is an excellent guide on how to create pull requests and forks to request changes.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

   [CSS]: <https://devdocs.io/css/>
   [Python 3.10]: <https://www.python.org/downloads/release/python-3109/>
   [Here]: <https://www.dataschool.io/how-to-contribute-on-github/>
