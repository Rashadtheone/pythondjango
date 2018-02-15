#LearningPython 

##Resources 
    - GA Git respositories

###Calculator 
    - Semicolon is similar to starting a function, or ending a line
    - Variables don't need type declarations
    - Indentation can be 'closing' a method or action 
    - python filename.py runs python file in terminal

##RefactorFizzBuzz
    - For Loops range is setting the starting point of the loop. 
    - elif is else if
    - Dictionaries and list replace arrays and objects
    - """ this is a comment """ 
    - Scope still matters. 
    - .get and key value pairs are interchangable

##Django Tunr
    - Create Directory 
        - python3 -m venv myvenv 
    - Enter Envirorment 
        - source myvenv/bin/activate
    -Install Django 
        - pip install django~=1.11.0
    -Create Root of App
        - django-admin startproject mysite .  // Don't forget the period ! 
    -SetUp Database 
        - PSQL
            > CREATE DATABASE appName;
            > CREATE USER appuser WITH PASSWORD 'appPassword';
            GRANT ALL PRIVILEGES ON DATABASE appName TO appuser;
    - Edit Default Settings for Database ! 
        - 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        - 'NAME': 'tunr',
        - 'USER': 'tunruser',
        - 'PASSWORD': 'tunr',
        - 'HOST': 'localhost'
    - Create Modals 
        - python manage.py startapp componentName  //start app is different than start project!
        - add component to list of installed apps! in your settings!
    - Create Migrations 
        - python manage.py makemigrations appName
    - Apply Migrations  
        - python manage.py migrate appName





