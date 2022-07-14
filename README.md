# Project Setup

Name:

UCID:

## Introduction

For this assignment you need to set up Docker and then deploy this website to Heroku. Follow the instructions below and
watch the video that is the conceptual overview of this unit and the video that shows you how to complete the
assignment. You will need to signup for [Dockerhub](http://www.docker.com) and [Heroku](http://wwww.heroku.com).

To complete the assignment you need to put a link to the running site on heroku and the badge that shows the production
workflow working where indicated below.

### Unit Videos

1. Conceptual Overview - [Here](https://youtu.be/u4RaG_elMbQ)
2. Slides - [Here](dj.pdf)
3. How to complete assignment - [Here]()

## Put the production workflow badge here

[![Production Workflow]()]()

## Put a link to your Production Heroku Deployment Here

* [Production Deployment](https://kwilliam-prod.herokuapp.com/)

## Instructions

1. Clone this repo to your local
2. Create an account with Heroku, create an app for production and an app for development
3. Create a new repo in Docker hub

### Setup Docker and Heroku Credentials In the Repository Settings under Action -> Secret

4. In your newly created GitHub repository, add new repository secrets for DOCKER_USERNAME, DOCKER_PASSWORD,
   HEROKU_API_KEY (Values are DOCKER_USERNAME: your docker hub username; DOCKER_PASSWORD: your docker hub password;
   HEROKU_API_KEY: API key from the heroku app)

#### GitHub Notes:  Set the action secrets repository in: -> settings -> actions -> secrets

#### Heroku Notes: Get the heroku API key from account in: -> applications -> create authorization button

### Change GitHub Actions Workflows for Prod

5. Change line 42 to have your docker repo address in: .github/workflows/prod.yml
6. change lines 58 to have your heroku app name in: .github/workflows/prod.yml
7. change line 59 to have your heroku email in: .github/workflows/prod.yml
8. Push code to your local repo and check for any errors and fix any errors that appear when the workflow is running.
   You can check the workflow in the
   actions.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest

### Future Notes and Resources

* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
