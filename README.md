# Django IT Jobs
> REST Web API built with Django and Django REST Framework.

## Table of contents
* [General info](#general-info)
* [How to run it locally](#how-to-run-it-locally)
* [Endpoints](#endpoints)
* [Technologies](#technologies)
* [Status](#status)

## General info

Django IT Jobs is a web API built with Django and Django REST Framework. Application stores job offers and applications in database - SQLite. User is able to fetch job offers and apply for them. Authentication and authorization is based on JWT. (JSON Web Token). Admin uses dedicated admin panel to access data from database.

## How to run it locally

1. Clone repository:
```
git clone https://github.com/b-grochal/django-it-jobs.git
```
2. Create virtual environment:
```
python -m venv env
```
3. Activate created virtual environment:
```
env\Scripts\activate
```
4. Navigate to folder with project:
```
cd django-it-labs
```
5. Install all necessary packages from requiremets file:
```
pip install -r requirements.txt
```
6. Perform migrations:
```
python manage.py migrate
```
7. Run application: 
```
python manage.py runserver
```

## Endpoints
`GET /api/jobs/` - Get list of jobs <br />
`GET /api/jobs/id` - Get details of specified job <br />
`POST /api/jobs/applications` - Apply (send your personal data) for the job <br />
`POST /api/login` - Login into your account <br />
`POST /api/register/` - Create new accoutn <br />
`POST /api/login/refresh` - Refresh access token <br />

## Technologies
* asgiref 3.4.1
* Django 4.0
* django-cors-headers 3.10.1
* django-filter 21.1
* djangorestframework 3.13.1
* djangorestframework-simplejwt 5.0.0
* PyJWT 2.3.0
* pytz 2021.3
* sqlparse 0.4.2
* tzdata 2021.5

## Status
Project is finished at the moment.
