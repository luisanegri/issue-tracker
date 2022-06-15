
[![Build Status](https://travis-ci.org/luisanegri/issue-tracker.svg?branch=master)](https://travis-ci.org/luisanegri/issue-tracker)

# Issue Tracker Web App
Demo: https://issue-tracker-django.herokuapp.com/

## Overview

> A web application created in Python and Django.


## UX


__Profile Page: Navigation bar > Profile__

The Profile page shows the user's username, the issues the user added and its details.
It also allows users to perform CRUD (Create, Read, Update and Delete) on any issue.

* View details about the issues added:
1. Click on the issue you want to read about

* Adding an issue:
1. Click on the button 'Add'
2. Fill out the form

* Editing an issue:
1. Click on the issue that needs to be edited
2. Click on the button 'Edit'
3. Fill out the form

* Deleting an issue:
1. Click on the issue that needs to be deleted
2. Click on the button 'Delete'

* Buy a feature:
1. Click on the feature you want to buy
2. Click on the button 'Add to cart'
3. On the navigation bar click on 'Cart'
4. The 'Cart' page displays your order
5. Click on the button 'Checkout'
6. Review your order and fill out the form

__Issues Page: Navigation bar > Home__

This page displays all issues added by any user. 
Issues are split into two columns - Bugs and Features - which are organised by the number of upvotes in a descending order.
The number of upvotes is shown on the accordion with a thumbs up icon.

* Visualise issue's description and status:
1. Click on the issue

* Read more details about an issue:
1. Click on the issue
2. Click on the button 'Details'

__Details Page: Navigation bar > Home > Issue > Detail__

Read more details about the issue, such as: name, description, status (to do, doing, done), label (bug or feature), date created and created by.

The status changes colour according to the status. 

* Upvote:
1. Click on the thumbs up icon

* Buy:
If the issue is labeled as a feature a button 'Add to cart' will be displayed on the page, except when the status of the feature is done.
1. Click on the button 'Add to cart'
2. On the navigation bar click on 'Cart'
3. The 'Cart' page displays your order
4. Click on the button 'Checkout'
5. Review your order and fill out the form

* Comment:
1. Click on the button 'Add'
2. Fill out the form

* Edit a comment:
1. Click on the button 'Edit'
2. Fill out the form


## Features

* User authentication - Register, Login, Logout
* User Profile
* Search bar
* Full CRUD functionality
* E-commerce

## Technologies

* HTML
* CSS
* Font Awesome
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
