
[![Build Status](https://travis-ci.org/luisanegri/issue-tracker.svg?branch=master)](https://travis-ci.org/luisanegri/issue-tracker)

# Issue Tracker Web App
Demo: https://issue-tracker-django.herokuapp.com/

## Overview

> A full stack web application created in Python and Django.

## Features

* User authentication - Register, Login, Logout
* User Profile
* Search
* Full CRUD functionality
* E-commerce

## Technologies

* HTML
* CSS
* Bootstrap
* Python
* Django
* Stripe
* PostgreSQL
* Amazon Web Services
* Heroku

## Deployment

* This project was deployed at Heroku

1. Create requirements.txt 

        pip3 freeze --local requirements.txt
        
2. Create Procfile

        echo web: python app.py > Procfile
        
3. Create [Heroku](https://www.heroku.com/) App 
4. Set Config Vars:  IP and PORT, secret keys (Stripe, AWS, app) 
5. Login to Heroku on the terminal

        Heroku login
        
6. Deploy to Heroku

        Scale the app's web process to 1 dyno: heroku ps:scale web=1
        git remote add heroku app
        git push heroku master
