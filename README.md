
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

## Testing

1. User Authentication:

- Login page
* Left username and password required fields blank > Output: 'Please Fill out this field'. (Passed)
* Entered a non existent username > Output: 'Your username or password are incorrect'. (Passed)
* Entered a wrong password > Output: 'Your username or password are incorrect'. (Passed)
* Entered a correct username and password > Output: 'You have successfully logged in'. (Passed)

- Registration page
* Left username, email address, password and password confirmation > Output: 'Please Fill out this field'. (Passed)
* Entered a username not allowed. < Output: 'Enter a valid username. This value may contain only English letters, numbers, and @/./+/-/_ characters.'
* Tried to log in without providing an email address > Output: 'Email addresses must be unique.' (Passed)
* Entered an email address without @ > Output: 'Please include an @ in the email address' (Passed)
* Entered an email address already registered > Output: 'Email addresses must be unique'. (Passed)
* Entered an username that already exists > Output: 'A user with that username already exists.' (Passed)
* Entered a wrong password confirmation > Output: 'Passwords do not match'. (Passed)
* Entered correctly an username, email address, password and password confirmation > Output: 'You have successfully logged in'. (Passed)

2. Create, Read, Update and Delete Issues

- Create
* Left name and description fields blank > Output: 'Please Fill out this field'. (Passed)
* Entered a name, description and selected the type of issue (which is by default a bug, so it will never be blank) > Output: 'New issue created successfully!'. (Passed)
* When a new issue is created, the issue is saved in the database and the page is redirected to 'My Issues' page where the issue is displayed. (Passed)
* Issue is also displayed on 'All Issues' page.

- Read
- Edit Issue
* Left name and description fields blank > Output: 'Please Fill out this field'. (Passed)
* Entered a different name, description and type of issue > Output: 'Your issue was updated successfully!'. (Passed)
* When an issue is edited, the issue is saved is updated in the database and the page is redirected to 'My Issues' page where the issue is displayed. (Passed)
* Issue is also displayed on 'All Issues' page. (Passed)

- Delete Issue
* When clicking on Delete button the issue is deleted from the database, and from the pages 'My Issues' and 'All Issues'. (Passed)

3. Create and Update Comments

- Create Comment:
    - Clicked on the button 'Comment' > Brings to another page with a form. (Passed)
    - Left the input field blank > 'Please Fill out this field'. (Passed)
    - Entered a comment. The comment is saved in the database, and the page is redirected to the previous page where the comment is displayed with the username, date and time. (Passed)

- Edit a Comment
    - Clicked on the button 'Edit' > Brings to another page with a form. (Passed)
    - Left the input field blank > 'Please Fill out this field'. (Passed)
* Entered a new comment > Page not found (404). (Failed)

4. Upvote
* Clicked on the button 'Upvote' the page is redirected to 'Issues' page and displayes the message 'Upvoted successfully!' (Passed)
* Upvote is saved in the database and displayed in the badge placed in the accordion. (Passed)
* The upvoted issue is displayed on the top of the issues that have less upvotes. (Passed)

5. Cart
* Clicked on the button 'Add to cart' the page is redirected to 'Issues' page and displays the message 'Feature added to cart'
* Cart page: Feature is added to cart. (Passed)

6. Checkout
* Proceeded with checkout, the product overview is displayed (Passed)
* Proceed with payment by filling out the form and using Stripe's test card number 4242 4242 4242 4242 (Passed)

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
