# GereTonAsso

Coming soon

### How to install?
Clone me, create a virtual environment with [virtualenv](https://virtualenv.pypa.io/en/stable/) (*!!! maybe you have to install !!!*) and activate it:
```shell
$ git clone https://github.com/JBthePenguin/GereTonAsso.git
$ cd GereTonAsso
$ virtualenv -p python3 env
$ source env/bin/activate
```
Install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/)):
```shell
(env)$ pip install -r requirements.txt
```
Make the migrations:
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
Create a *superuser*:
```shell
(env)$ python manage.py createsuperuser
```

### How to use?
Start the server (the virtual environment have to be activated):
```shell
(env)$ python manage.py runserver
```
With your favorite browser, go to url:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the home page and acces to the lists.
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) to use the admin site.
