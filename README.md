# Zero to api

Creating an authenticated api from scratch, with django, django rest framework, and djoser.

## Prerequistes to follow the presentation
- pipenv and installation of python 3.6+ 
- a restful testing program, this is going to act as our client (more on that soon):
    - [Firefox rest client add on](https://addons.mozilla.org/en-CA/firefox/addon/restclient/)
    - [Chrome rest client add on](https://chrome.google.com/webstore/detail/rest-ape-advanced-api-tes/ohalacbnhbfllngjcgnejjdgmhbkcnld?hl=en)
- I'm going to do this all in Ubuntu, so instructions will be a bit different but similar for mac and windows.
    - On windows you'll need to use powershell, WSL (windows subsystem for linux)
    - On Mac you'll need to use terminal or bash.
    - If you're using VSCode then you should have a terminal built in.

### Knowledge that's nice to have but not necessary
- git (if you want to clone the repo later.)
- Some basic knowledge of django is great but it's alright if you don't. What do you need to know?
    - It's a web framework that you can serve small and large websites (how big? Instagram big).

## What are we going to do?
- talk about restful api
    - Why it's important?
    - What is it?
    - Who uses it?
    - Some places where you can discover some more RESTful APIs for yourself.

- the full shabang of building our RESTful api.
   - create our environment and install the packages.
   - create a django project in our environtment.
   - add the djangorestframework and djoser packages
   - hook up the authentication api and configure it to our web project.
   - create an app with models (and add them to the admin), serializers, views, urls (more on all of these later)
   - create a RESTful api for the app above and hook it up to our web project.
- If we have time we can discuss.
   - Add some javascript that can "consume" our api.
   - Deploy to heroku.
   - Add a lot of data from an [opendata platform](https://www.kaggle.com/ma7555/cat-breeds-dataset) using management commands.

## The What, Why, Who of RESTful APIs.
A RESTful api is basically a way to transfer information from a server (where you store information and do tasks) to a client. A client can be a mobile app, a website (loaded on your computer), games that store high scores or anything that will "consume" information.

- If you want more information on this you take a look here.
[![A video about restful apis.](http://img.youtube.com/vi/7YcW25PHnAA/0.jpg)](https://www.youtube.com/watch?v=7YcW25PHnAA&t=1s)

- Used by mobile apps, all website you go to, iot devices and much more!
- Used by data scientists (and machine learning) professionals to get their data.

- Here's some RESTful APIs that you folks can use in your own projects:
    - [Awesome Public APIs](https://github.com/public-apis/public-apis): A list of public free APIs for your projects.
    - [Google API Library](https://console.developers.google.com/apis/library): Want to do something fancy with computer vision or anything on the google cloud platform? You can use those APIs in that link.

Note: We're essentially going to create one of these.

## What are the packages we're going to use and why are we going to use them.
- we're going to be creating the api using the following packages:
    - [Django](https://www.djangoproject.com)
        - this is a web framework and an orm (Object Relationship Mapper) which is basically just an sql interface (so creating tables, and read/write/update/delete from those tables as well).
    - [Django Rest Framework](https://www.django-rest-framework.org/)
        - this is going to allow us to really simplify the api creation process.
        - We're also going to use this for login with tokens as well.
    - [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
        - this is going to handle our registration (through the api).

## Creating your environment
The following is going to be in your terminal/powershell/wsl.

- Create a folder for your project.
    - you could use `mkdir my-super-cool-project-lol`

- Create a virtual environment
- if you're using python virtualenvs (most of you)
1. `python3 -m venv ./venv`
    - This is going to create a virtual environment so that you can install django and other packages isolated from other environments.
2. `source venv/bin/activate`
    - This is going to start your environment.
3. `python3 -m pip install <package name>`
    - you're going to use this to install the packages needed.


- if you're using pipenv (many of you won't so you can ignore the next two points)
1. initialize your virtualenv with the following command
    `pipenv shell --python=3.7`
2. install the packages
    `pipenv install <package name>`
    (where ever you see `python3 -m pip install` you can replace it with `pipenv install`)

Note:
If you're totally stuck during the tutorial at any time you can do the following.
- `git clone https://github.com/dgmouris/zero_to_api.git`
    do a git clone of the repository
- Create your environment, and init initial (look above)
- Install all the packages required.
    - `python3 -m pip install -r requirements.txt`
- You'll need to do this in a completely separate folder/environment, if this is your first time through just ignore this note and come back later if you're stuck.

## Installing the packages.
- Django installation:
    - `python3 -m pip install django`
        - this is going to install the latest version of django.
- Django rest framework installation
    - `python3 -m pip install djangorestframework`
        - latest version.
- Django Djoser
    - `python3 -m pip install djoser`
- Django Cors Headers (so any client can access it.)
    - `python3 -m pip install django-cors-headers`

## Starting a django project
- Django has a set of command line programs to help you set up your project.
    - if you type in django-admin in your shell then it should pop up with a bunch of options.
- We're going to use the `django-admin.py startproject` to begin the project.
    - I'm calling mine zero_to_api. (eg. `django-admin.py startproject zero_to_api` if you want to do the same.)
- Now you should see the barebones of your project (go into the folder `cd zero_to_api` your project name)
    - in the folder of your project you should see the following files:
        - `manage.py` a file that helps gives us handy things that will help us with our project
            - migrations for our database (this is the orm part)
            - run a local server so that we can test stuff on our computer
            - this is a bit like `django-admin.py`, but more specific to your website.
            - a lot of other handy things that we might get to.
        - a folder which has the same name as your project (`zero_to_api`) which contains the following files
            - `urls.py`
                - this is going help us define our endpoints (ie. http://localhost:8000/v1/auth/token/ login, but note we haven't created this yet.)
            - `settings.py`
                - all of the static settings variables that are essential to our app.
                - as well it defines the apps (parts of our website) that are going to be used.
            - `wsgi.py`
                - we're not going to worry about this today.
                - For curious cats, this is how Django interfaces with webservers (More info [here](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/))
        - `db.sqlite3`
            - this is going to be the database we're going to use for today.
            - Note: This is only going to show up once you "migrate", we're looking at this next so it's going to pop up shortly.

## Getting started doing some django.
- go into your project folder. Let's see if we can run django! in your terminal run
    - `python manage.py runserver`
- now if you look at your terminal you will see something like the following:
![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_apply_migrations.png)
- what this means is that django wants to make some stuff in our database and we also want it to do that!
- running migrations (a simplified overview for our talk.)
    - `python manage.py makemigrations`
        - this checks to see if anything changed in your project that will need to modify your database. Note: All of the models (pythonic way of interacting with the database) are from external packages, so this is only going to have changes if we create our own models.
        - this is mostly going to apply when you're writing your own models (like tables in sql except for python)
    - `python manage.py migrate`
        - this applies the migrations to your database.
    - Having problems here can become a tough thing to cover as it can be a bit complicated, we won't be doing that today.

- Let's run them now! in your terminal (that's inside your project) run the following command
    - `python manage.py migrate`

- now if you run your local server (`python manage.py runserver`) you won't get any warnings.

Note: You should be able to see `db.sqlite3` in your folder now too!

## Let's start adding configuring our apps (which are parts of our website).
- Let's add the authentication which will add the login endpoints to our website (you'll see)

- first let's go to our settings.py
    - go to your `INSTALLED_APPS`, and let's add a couple.
        - add the following lines within the existing list.
```python
INSTALLED_APPS = [
    # my installed apps
    'django.contrib.auth', # should already be there.
    #...other packages ...
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders'
]
```

- To the middleware you'll have to use CorsMiddleware right before the CommonMiddleware this is really really important if you want to use multiple clients. You'll also be specifying that any client can access our api with `CORS_ALLOW_ALL_ORIGINS = True`
```python
MIDDLEWARE = [
    # other middlewares
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # more middlewares
]

# Cors (you can add this to the bottom)
CORS_ALLOW_ALL_ORIGINS = True
```
Note: This makes it so that you can control who can access your website, you can make it so one or multiple domains (eg. www.github.com), one or multiple ips (eg. 127.0.0.1) can access your site.
- now if you go back to your terminal and run your local server (`python manage.py runserver`)
    - you should see something similar to the first time. We need to add the models from external packages so those packages can access the database using their models!
        - show picture ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_apply_migrations_2.png)

- let's run our migrations again so that we can apply the changes to the database!
    - `python manage.py makemigrations`
        - this will tell us no changes detected because we haven't changed/created models of our own, we just need to add new packages.
    - `python manage.py migrate`
        - this is going to add some tables from the django-restauth package

## Let's add the django-restauth login endpoints to our package.
- urls.py package add the following line in the `urlpatterns list`
```python
from django.contrib import admin
from rest_framework.authtoken import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/token/', views.obtain_auth_token),
]
```
That's what you `urls.py` should look like!

- To be able to use this from your rest client you'll need specify the authentication classes that your project uses. We're using token authentication to create our api. In your `settings.py` add the following object.
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication', # we're going to remove this
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}
```

## Exploring endpoints and adding a user.
- Let's run our server now (`python manage.py runserver`)
- if you go to http://localhost:8000 you'll get a 404
    - shown here ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_404_with_endpoints.png)
- this is not a bad thing. this is a good thing, let's go explore them.
    - http://localhost:8000/admin/
        - but I can't login! what's going on! oh my god dan has such cute cats and I can't concentrate!
        - we'll deal with this very soon.
    - http://localhost:8000/v1/auth/users/
        - You should see your credentials aren't provided! To be able to see all of the options you'll have to login to your admin. We'll do that next. should look like this.
        ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_403_forbidden.png)
        - but we have to do a few more things to get this to work.
- let's add our first user (yourself)
    - go back to the terminal and write the following command
        `python manage.py createsuperuser`
        - answer the questions should look like this.
        ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_createsuperuser.png)
    - let's go test it.
        1. run your server
        2. go to http://localhost:8000/admin/
        3. if you can login you've created your user!
    - Now you can go to http://localhost:8000/v1/auth/users/ and you'll see yourself there.
        ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_users_success.png)

## Testing your api!
- let's open your rest client! I'm using the "Firefox Rest Client" add on.
    Note if you don't have one of these please see the links in the "Prereqs section".
- Comment out the line in your `settings.py` in your `REST_FRAMEWORK` object
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication', # we're going to remove this
        # ...other auth classes...
    ]
}
```
- to walk you through this do the following steps.
1. open your rest client
2. use the "POST" method
3. enter in the following url `http://localhost:8000/v1/auth/token/`
    - You may need to add the header: `Content-Type: application/json`
4. in the body enter the following parameters.
    - username: the_user_name_you_used_earlier
    - password: the_password_you_entered_earlier
    the body should look like this.
```json
{
    "username": "daniel",
    "password": "temptemp"
}
```

5. press send, and you should see the key! You should see something like this.
![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_rest_client_success.png)

- !IMPORTANT! What this key (or token) is used for is to login your user later on, keep it on hand!

- You'll need to add the `'rest_framework.authentication.SessionAuthentication'` line whenever you access the admin (more on that later).

## Let's create an app (part of your website.) that requires authentication and we're going to make it accessible.
- how do we do this?
- First we're going to create the app. I'm calling mine cats.
    - to do this you have to run the following line in your terminal (and your project root folder.)
        `python manage.py startapp cats`
    - you should now see a "cats" folder with a few things, that I'm going to cover as we need them.
- let's add cats to our installed apps so that our website knows to use that part of the site:)
    - go to the zero_to_api folder in your project root.
        - in the settings.py `INSTALLED_APPS` list add the following lines.
```python
INSTALLED_APPS = [
    # all of other apps.
    'cats',
]
```

- What are apps?
    - Apps are essentially a piece of functionality for your site, django tries to keep different pieces of functionality separate from other pieces. Account management for example, is different than any cats functionality we have in our app.

## Creating some models
- Now let's first add your models in the `models.py` in your cats folder (or what ever your created.)
    - models are like tables in your database that you can manipulate with python.
    - We're going to create two models and add them.
        - Cat Breed
        - Cat
    - Here's what the models are going to look like.
```python
from django.db import models

class CatBreed(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return F"{self.name}"

class Cat(models.Model):
    name = models.CharField(max_length=255)
    cat_breed = models.ForeignKey(CatBreed,
                                  on_delete=models.SET_NULL,
                                  null=True)

    def __str__(self):
        return F"{self.name}, {self.cat_breed}"

```

- What are models you ask?
    Models do a few things in Django:
        - First generally maps to a single database table, the fields provide the "schema" (essentially structure) of that table.
        - It also gives you a pythonic interface to add remove update and delete data in your database.

Note: if you want to learn more about django models you can take a look here [Model docs](https://docs.djangoproject.com/en/3.1/topics/db/models/)

## Let's talk about migrations
- Let's do the "makemigrations" because we've made changes to our own app that we've created with the following command
    - python manage.py makemigrations
        - the output should look something like this:
            ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_cats_make_migrations.png)

- If that was successful then we can apply our migrations with the following command
    - python manage.py migrate
        - the output should look something like below
            ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_cats_apply_migrate.png)

- What are Migrations you ask?
    - Any changes in your models need to be reflected in your database tables (see Models as well)
    - So "makemigrations" creates a special Django python file, that will create pending changes to our database (we can edit this too).
    - Once we've done the above we execute "migrate" it's going to execute this file which will change our database (`db.sqlite3` for us if you're wondering)

- Now that we have tables in our database, let's add them to the admin project so that we can add some data
    - go to the admin.py in your cats folder and modify it the following contents.
```python
from django.contrib import admin

from .models import Cat, CatBreed

admin.site.register(Cat)
admin.site.register(CatBreed)

```
This makes it so that you can add rows (data) to your models (in this context read: database tables) via the admin.

- now go back and run your server and login to the admin page (http://localhost:8000/admin/)
    - you should see `Cat` and `CatBreed` models included.

- Click on each of them and add some data. I already have some:)

- That's Great but....
    - You guys want this to be accessible via an api! That's the goal of today!
    - So let's create one.

Note: If you want to learn more about the admin you can go look at the [admin docs](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)

## Let's create our restful api!
- let's make it accessible, so that we can add cats from our client!

## let's make some serializers
- In your `cats` Folder we're going to create a `serializers.py` file.
    - this is going to serialize our data, I'm not going to go into this in depth, but you can think of them as something that allows you have the functionality to modify your models, as well as get data from them via an api.
        - for more information go to http://www.django-rest-framework.org/api-guide/serializers/
    - our serializers are going to look like the following and are going to use the ModelSerializer, they look like this.
```python
from .models import Cat, CatBreed

from rest_framework import serializers

class CatBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatBreed
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
```

## let's make some viewsets
- now that we have to create viewsets, in the django rest framework documentation they define it as follows.
    "ViewSet classes are almost the same thing as View classes, except that they provide operations such as read, or update, and not method handlers such as get or put."
    http://www.django-rest-framework.org/api-guide/viewsets/
    - so you can think them as django views (which I won't get into today but you can ask me about it later.)
    - in your views.py file your viewsets are pretty easy they use the following:
        - a queryset which you can think of the data that your viewset is going to use.
        - your serializer.
    - your serializers will end up looking like the following if you look at the documentation:
```python
from django.shortcuts import render
from rest_framework import viewsets

from .models import Cat, CatBreed
from .serializers import CatBreedSerializer, CatSerializer

class CatBreedViewSet(viewsets.ModelViewSet):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
```

## let's hook it up to the urls with the django rest framework "router"
- Let's hook it up to our urls so that we can use it!
    - create a `urls.py` file in your cats folder.
    - now we're going to include a router which is a bit like urls in django, this adds our viewsets to a url path.
    - it should look like this:
```python
from rest_framework import routers
from .views import CatBreedViewSet, CatViewSet

router = routers.DefaultRouter()
router.register(r'cat-breeds', CatBreedViewSet)
router.register(r'cats', CatViewSet)

urlpatterns = router.urls
```

- This is going to add a bunch of paths to each url, a get, update, create, list and delete view of the items of your data in your remove
- Now that we have our urls defined in our app we have to add it to the overall web project.
    - it's one line of code in the `zero_to_api/urls.py` file. the line is:
```python
    path('v1/catapp/', include('cats.urls')),
```

- This will connect all of the routes from our app to the entire project.

## What did I just do?
- run your localserver and go to the following destinations in your browser you should see something crazy cool!
    - http://localhost:8000/v1/catapp/cats/
    - http://localhost:8000/v1/catapp/cat-breeds/
- Congratulations you just created your first api!

## But wait there's more!
- Can we access this from our REST Clients? Yes!

## Enable the api for the "POST" method
- Let's enable this for the post method so that we can add something.
    - we need to enable token authorization so that we can post! or else we're going to get some csrf failure.
    - remove the `rest_framework.authentication.SessionAuthentication`  in you `zero_to_api/settings.py` file. You might have already done this but this is super important!
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication', # Remove this now!!!
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}

```

- this will also allow us post as well as give us functionality private.
- now if you look at the following picture you should be able to add a new cat! via an api (using arc)
    ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_rest_client_add_cat.png)
Note: On post requests you need to add a traling slash to all requests (unless you specify otherwise in the settings!)

Note: You can go here to learn more about [django rest framework settings](https://www.django-rest-framework.org/api-guide/settings/)

## Let's make our api Private!
- we don't really care if people can see our cat types, but we don't want people to know our cat names!
- let's make the cat types public, but let's make the cats private, where you need to login.
- in your viewsets.py file you need to "include permissions" add the following line if you don't want to make it public
```python
# other imports ....
from rest_framework import viewsets, permissions # we added the permissions!

# ... other code
class CatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] # we added this line!
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

```

- the entire file should look like this:
```python
from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Cat, CatBreed
from .serializers import CatBreedSerializer, CatSerializer


class CatBreedViewSet(viewsets.ModelViewSet):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
```

- now if you go to http://localhost:8000/v1/cats/ it'll show you that you don't have any credentials, and won't permit you yay!
    - How can I test this? Rest Client to the rescue.

Note: If you want to learn more about permissions, you can go to the fantastic documentation here [permissions docs](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)
If you want to learn more about viewsets you can look here (viewset docs)[https://www.django-rest-framework.org/api-guide/viewsets/]

## I want to access my private stuff!
- go to your advanced rest client, use the "POST" method and put in the login url (http://localhost:8000/v1/auth/token)
- put in your credentials in the body (like we did the first time) and copy the key somewhere handy so you can copy it.
    if you need a refresher see: ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_rest_client_success.png)
- now we're going to access our stuff via token authentication!
- Use the "GET" method and enter the url "http://localhost:8000/v1/catapp/cats/"
- in your advanced rest client select the "Headers" section
    - in the header name enter "Authorization"
    - in the header value enter "Token <your-super-private-key>"
- it should look like the following:
    - Step 1 add the token:
![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_rest_client_add_token.png)
    - Step 2 Get the cats:
![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_rest_client_cat_with_token.png)
    - Step 3 Profit (and pet cats)

## Djoser we installed it, but we haven't used it yet
- Djoser will allow you to sign up users and deal with all of the complications of doing that.
- You'll need to add a dummy backend for email, you'll need to configure one at some point if you want to deploy. The following is going to go into your `settings.py`.
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This is essentially going to show you emails in your console, which is what we need for now.
- If you go to `http://localhost:8000/v1/auth/users/` you should be able to register a new user.
- You can also go to the rest client and use the "POST" method to `http://localhost:8000/v1/auth/users/` with the following body:
```json
{
    "email": "rick@rick.com",
    "username": "rick",
    "password": "temptemp"
}
```

- then you can login at `http://localhost:8000/v1/auth` with the body
```json
{
    "username":"rick",
    "password": "temptemp"
}
```

- and then access our private cats api here `http://localhost:8000/v1/catapp/cats/` with the Header
`Authorization: Token <token from above here>` to see the information.

## Conclusions
- What have we done here?
   - created and used a virtual environemnt.
   - created a django project
   - added the django, djangorestframework, djoser, django-cors-headers packages
   - hooked up the authentication api and configured it to our web project.
   - created an app with models (and added them to the admin), serializers, views, urls,
   - created an api for the app above and hooked it up to our web project.
- This code doesn't use best practices necessarily so look them up if you are worried.
- Feel free to use this, I hope it was helpful.
- If you liked this talk/tutorial and you want to help me, star the repo, add me on linkedin if you'd like as normally I share when edmontonpy is.

## Success, Congratulations you're awesome!
- you've reated your first RESTful so now go conquer the world! Apps, Websites, IOT, and what ever else you want to do!
- Hopefully this was useful and you're as excited as [Steve Ballmer](https://youtu.be/hOq85MuBTXg?t=14).

## Extras
   - Add some javascript that can "consume" our api.
   - Deploy to heroku.
   - Add a lot of data from an [opendata platform](https://www.kaggle.com/ma7555/cat-breeds-dataset) using management commands.

## Resources
You're thinking to yourself, I can do this and I want to learn more. Here's some more resources that you can go check out.
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)

