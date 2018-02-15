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

[Link To Repo!](https://github.com/Rashadtheone/djangotrail)

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
    - Apply ALL Migrations ! 
        - python manage.py migrate


    How were you first made aware of it? 
        - My buddy told me it's a widely used tool
    What problem does it solve?
        - It's similar to rails, it allows you to develop websites quick
    How does it solve the problem (conceptually)?
        - lessens the feeling of setting up a large scale app. 
    What are the alternatives?
        - Rails
    What are 3 interview questions one might be asked about this technology?
    1) Explain what is Django?

    Django is a web framework in python to develop a web application in python.

    2) Mention what are the features available in Django?

    Features available in Django are

    Admin Interface (CRUD)
    Templating
    Form handling
    Internationalization
    Session, user management, role-based permissions
    Object-relational mapping (ORM)
    Testing Framework
    Fantastic Documentation
    3) Mention the architecture of Django architecture?

    Django architecture consists of

    Models: It describes your database schema and your data structure
    Views: It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template
    Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page
    Controller: The Django framework and URL parsing
    4) Why Django should be used for web-development?

    It allows you to divide code modules into logical groups to make it flexible to change
    To ease the website administration, it provides auto-generated web admin
    It provides pre-packaged API for common user tasks
    It gives you template system to define HTML template for your web page to avoid code duplication
    It enables you to define what URL be for a given function
    It enables you to separate business logic from the HTML
    Everything is in python

    What did you decide to learn today?
        Today I learned about Django, and the basic syntax of python    
    Why did you want to learn it?
        I've heard Python and Django make a good Stack
    What did you do to try and learn it? What process did you follow?
        I worked in a group with Wade and Shelly, we covered some tutorials,
        and knocked out some basic application builds. 




