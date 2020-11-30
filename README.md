# Zero to api

Creating an authenticated api from scratch, with django, django rest framework, and django rest auth.

## Prerequistes to follow the presentation
- pipenv and installation of python 3.6+ 
- a restful testing program, this is going to act as our client (more on that soon):
    - [Firefox rest client add on](https://addons.mozilla.org/en-CA/firefox/addon/restclient/)
    - [Chrome rest client add on](https://chrome.google.com/webstore/detail/rest-ape-advanced-api-tes/ohalacbnhbfllngjcgnejjdgmhbkcnld?hl=en)
- git (if you want to clone the repo later.)
- some basic knowledge of django, but I'll try to fill in the gaps.
- I'm going to do this all in Ubuntu, so instructions will be a bit different but similar for mac and windows.

## if you want to follow along while I present (or look at this afterwards)

1. do a git clone of the repository
`git clone https://github.com/dgmouris/zero_to_api.git`

- if you're using python virtualenvs
### TODO ###


- if you're using pipenv 
2. initialize your virtualenv with the following command
`pipenv shell --python=3.7`
3. install all the packages
`pipenv install`
4. try not to jeer me as I talk :)


## What are we going to do?
- talk about restful apis

- the full shabang of building our api below.
   - create a django project
   - add the djangorestframework and djoser packages
   - hook up the authentication api and configure it to our web project.
   - create an app with models (and add them to the admin), serializers, views, urls,
   - create an api for the app above and hook it up to our web project.
- If we have time
   - Add some javascript that can "consume" our api.
   - Deploy to heroku.
   - Add a lot of data from an (opendata platform)[https://www.kaggle.com/ma7555/cat-breeds-dataset] using management commands.

## What is a restful api, and who uses it?

A RESTful api is basically a way to transfer information from a server (where you store information and do tasks) to a client. A client can be a mobile app, a website (loaded on your computer), games that store high scores or anything that will "consume" information.

- If you want more information on this you take a look here.
[![A video about restful apis.](http://img.youtube.com/vi/7YcW25PHnAA/0.jpg)](https://www.youtube.com/watch?v=7YcW25PHnAA&t=1s)

- Used by mobile apps, all website you go to, iot devices and much more!
- Used by data scientists (and machine learning) professionals to get their data.


## What are the packages we're going to use and why are we going to use them.
- we're going to be creating the api using the following packages:
    - [Django](https://www.djangoproject.com)
        - this is a web framework and an orm (Object Relationship Mapper) Basically just an sql interface
    - [Django Rest Framework](https://www.django-rest-framework.org/)
        - this is going to allow us to really simplify the api creation process
    - [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
        - this is going to handle our registration (through the api) as well as login.

## Creating your environment
- create a folder (I created mine)
    - you could use `mkdir my-super-cool-project-lol`
- I used `pipenv shell` to create a virtualenvironment which allows us to isolate packages to this project.
- you should see your virtual environment on the left hand side of your terminal


## Installing the packages.
- Django installation:
    - `pipenv install django`
        - this is going to install the latest version of django.
- Django rest framework installation
    - `pipenv install djangorestframework`
        - latest version.
- django djoser
    - `pipenv install djoser`
- django cors headers (so any client can access it.)
    `pipenv install django-cors-headers`

## Starting a django project
- django has a set of command line programs to help you set up your project.
    - if you type in django-admin in your shell then it should pop up with a bunch of options.
- We're going to use the `django-admin.py startproject` to begin the project.
    - I'm calling mine zero_to_api. (eg. django-admin.py startproject zero_to_api)
- Now you should see the barebones of your project.
    - a folder for you project
        - manage.py a file that helps gives us handy things that will help us with our project
            - migrations for our database (this is the orm part)
            - run a local server so that we can test stuff on our computer
            - this is a bit like `django-admin.py`, but more specific to your website.
        - a folder which has the same name as your project (zero_to_api) which contains the following files
            - urls.py
                - this is going help us define our endpoints (ie. http://localhost:8000/v1/auth/token/ login, but note we haven't created this yet.)
            - settings.py
                - all of the static settings variables that are essential to our app.
                - as well it defines the apps (parts of our website) that are going to be used.
            - wsgi.py
                - we're not going to worry about this today.
        - db.sqlite3
            - this is going to be the database we're going to use for today.

## Getting started doing some django.
- go into your project folder. Let's see if we can run django! in your terminal run
    - `python manage.py runserver`
- now if you look at your terminal you will see something like the following:
    show picture ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_apply_migrations.png)
- what this means is that django wants to make some stuff in our database and we also want it to do that!
- running migrations (a simplified overview for our talk.)
    - `python manage.py makemigrations`
        - this checks to see if anything changed in your project that will need to modify your database.
        - this is mostly going to apply when you're writing your own models (like tables in sql except for python)
    - `python manage.py migrate`
        - this applies the migrations to your database.
    - Having problems here can become a tough thing to cover as it can be a bit complicated, we won't be doing that today.

- Let's run them now! in your terminal (that's inside your project) run the following command
    - `python manage.py migrate`

- now if you run your local server (`python manage.py runserver`) you won't get any warnings.

## Let's start adding configuring our apps (which are parts of our website).
- Let's add the authentication which will add the login endpoints to our website (you'll see)

- first let's go to our settings.py
    - go to your `INSTALLED_APPS`, and let's add a couple.
        - add the following lines within the existing list.
```python
        # my installed apps
        'django.contrib.auth',
        ...other packages ...
        'rest_framework',
        'rest_framework.authtoken',
        'djoser',
        'corsheaders',
```

- To the middleware you'll have to use CorsMiddleware right before the CommonMiddleware this is really really important if you want to use multiple clients. You'll also be specifying that any client can access our api with `CORS_ALLOW_ALL_ORIGINS = True`
```python
MIDDLEWARE = [
    # other middles
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# Cors
CORS_ALLOW_ALL_ORIGINS = True
```

- now if you go back to your terminal and run your local server (`python manage.py runserver`)
    - you should see something similar to the first time.
        - show picture ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_apply_migrations_2.png)

- let's run our migrations again so that we can apply the changes to the database!
    - `python manage.py makemigrations`
        - this will tell us no changes detected because we haven't changed anything, we just need to add new packages.
    - `python manage.py migrate`
        - this is going to add some tables from the django-restauth package

## Let's add the django-restauth login endpoints to our package.
- urls.py package add the following line in the `urls_patterns list`
```python
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/token/', views.obtain_auth_token)
```

    PS. at the top you'll have to include the word include in the following line to get it to work.

```python
    from rest_framework.authtoken import views
    from django.urls import path, include
```

- To be able to use this from your rest client you'll need specify the authentication classes that your project uses. We're using token authentication to create our api.
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
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
        - there are a lot of options here, shown here: ### TODO ###
            ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_404_with_rest_auth_endpoints.png)
        - these are all of the endpoints that the restauth (the login api part to our website to work.)
        - but we have to do a few more things to get this to work.
- let's add our first user (yourself)
    - go back to the terminal and write the following command
        `python manage.py createsuperuser`
        - answer the questions.
    - let's go test it.
        1. run your server
        2. go to http://localhost:8000/admin/
        3. if you can login you've created your user!

## Testing your api!
- let's open your rest client! I'm using the "Advanced Rest Client" plugin for chrome.
- to walk you through this do the following steps.
    1. open your rest client
    2. use the "POST" method
    3. enter in the following url `http://localhost:8000/v1/auth/token/`
        - You may need to add the header: `Content-Type: application/json`
    4. in the body enter the following parameters.
        - username: the_user_name_you_used_earlier
        - password: the_password_you_entered_earlier
    5. press send, and you should see the key!

- the picture you should see is below.
### TODO ###
    ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_arc_test_api_1.png)

- What this key is used for is to login your user.

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
            'cats'
```

- What are apps?
    - Apps are essentially a piece of functionality for your site, django tries to keep different pieces of functionality separate from other pieces. Account, is different than cats.

## Creating some models
- Now let's first add your models in the models.py in your cats folder (or what ever your created.)
    - models are like tables in your database that you can manipulate with python.
    - We're going to create two models and add them.
        - Cat Types
        - Cats
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

## Let's talk about migrations
- Let's do the "makemigrations" because we've made changes to our own app that we've created with the following command
    - python manage.py makemigrations
        - the output should look something like this:
            ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_cats_make_migrations.png)

- If that was successful then we can apply our migrations with the following command
    - python manage.py migrate
        - the output should look something like below
            ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_cats_apply_migrate.png)

- Now that we have tables in our database, let's add them to the admin project so that we can add some data
    - go to the admin.py in your cats folder and modify it like the following picture.
```python
from django.contrib import admin

from .models import Cat, CatBreed

admin.site.register(Cat)
admin.site.register(CatBreed)

```

- now go back and run your server and login to the admin page (http://localhost:8000/admin/)
    - you should see "Cat" and "CatBreed" models included.

- Click on each of them and add some data. I already have some:)

- That's Great but....
    - You guys want this to be accessible via an api!
    - So let's create one.

## Let's create our restful api!
- let's make it accessible, so that we can add cats from our client!


## let's make some serializers
- In your cats Folder we're going to create a serializers.py file.
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

class CatBreedViewset(viewsets.ModelViewSet):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedSerializer

class CatViewSet(viesets.ModelsViewSet);
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

```


## let's hook it up to the urls with the django rest framework "router"
- Let's hook it up to our urls so that we can use it!
    - create a urls.py file in your cats folder.
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

- Now that we have our urls defined in our app we have to add it to the overall web project.
    - it's one line of code in the zero_to_api/urls.py file. the line is:
```python
    path('api/v1/catapp', include('cats.urls')),
```

- This will connect all of the routes from our app to the entire project.

## What did I just do?
- run your localserver and go to the following destinations in your browser you should see something crazy cool!
    - `http://localhost:8000/v1/catapp/cats/`
    - `http://localhost:8000/v1/catapp/cat-breeds/`
- Congratulations you just created your first api!

## But wait there's more!
- Can we access this from our REST Clients? Yes!

## Enable the api for the "POST" method
- Let's enable this for the post method so that we can add something.
    - we need to enable token authorization so that we can post! or else we're going to get some csrf failure.
    - you need to add the following lines to your zero_to_api/settings.py file. You might have already done this but this is super important!
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',),
}
```

- this will also allow us post as well as give us functionality private.
- now if you look at the following picture you should be able to add a new cat! via an api (using arc)
    ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_arc_create.png)


## Let's make our api Private!
- we don't really care if people can see our cat types, but we don't want people to know our cat names!
- let's make the cat types public, but let's make the cats private, where you need to login.
- in your viewsets.py file you need to "include permissions" add the following line if you don't want to make it public
```python
from rest_framework import viewsets, permissions

# ... other code
class CatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
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
    - How can I test this? If you logout from the admin you should be able to

## I want to access my private stuff!
- go to your advanced rest client, use the "POST" method and put in the login url (http://localhost:8000/v1/auth/token)
- put in your credentials in the body (like we did the first time) and copy the key somewhere handy so you can copy it.
    if you need a refresher see: ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_arc_test_api_1.png)
- now we're going to access our stuff via token authentication!
- Use the "GET" method and enter the url "http://localhost:8000/v1/catapp/cats/"
- in your advanced rest client select the "Headers" section
    - in the header name enter "Authorization"
    - in the header value enter "Token <your-super-private-key>"
- it should look like the following: ![alt text](https://github.com/dgmouris/zero_to_api/blob/master/images/zero_to_api_arc_get_authenticated.png)

## Djoser we installed it, but we haven't used it yet
- Djoser will allow you to sign up users and deal with all of the complications of doing that.
- You'll need to add a dummy backend for email, you'll need to configure one at some point if you want to deploy.
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
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
   - create a django project
   - added the django, djangorestframework, djoser, django-cors-headers packages
   - hooked up the authentication api and configured it to our web project.
   - created an app with models (and added them to the admin), serializers, views, urls,
   - created an api for the app above and hooked it up to our web project.
- This code doesn't use best practices necessarily so look them up if you are worried.
- Feel free to use this, I hope it was helpful.
- If you liked this talk/tutorial and you want to help me, star the repo, and if you're a connection on linkedin endorse me for python.

## Success, Congratulations you're awesome!
- you've reated your first app so now go conquer the world! Apps, Websites, IOT, and what ever else you want to do!

## Extras
   - Add some javascript that can "consume" our api.
   - Deploy to heroku.
   - Add a lot of data from an (opendata platform)[https://www.kaggle.com/ma7555/cat-breeds-dataset] using management commands.
