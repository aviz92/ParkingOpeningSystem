# ParkingOpeningSystem

------------------------------------------------------------------------------------------------------------------------

## Table of contents
* [General info](#General-info)
* [Setup](#Setup)

------------------------------------------------------------------------------------------------------------------------

## General info:

This ParkingOpeningSystem web application project is made with Django and open-cv as the backend.

This web application creates a very basic Parking Opening System site using Django. The site allows authors to create full apartment owners using the Admin site, and decide whether the gate will open for the tenant’s vehicle number (based on open-cv).

------------------------------------------------------------------------------------------------------------------------

## Setup

To run this app, you will need to follow these 4 steps:

1. Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/aviz92/ParkingOpeningSystem.git
```

2. Install Dependencies
```
pip install -r requirements.txt
```

3. Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```

4. Create Superuser 
```
python manage.py createsuperuser
```

5. After all these steps , you can start testing and developing this project. 
```
python manage.py runserver
```

#### That's it! Happy Coding!
------------------------------------------------------------------------------------------------------------------------
