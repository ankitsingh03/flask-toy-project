# Flask Toy Project

## Aim
You will implement the requirements which is written in the **USER-STORIES.md**.

## Requirements
1. Internet Browser
2. Internet Connection
3. Python Version 3.7+
4. Postgresql
5. List of all the dependencies in **requirements.txt**

## How To Run
1. Clone the project `git clone https://gitlab.com/mountblue/cohort-14-python/ankit_singh/flask-toy-project`
2. Open terminal in project directory.
3. Create virtual environment for project.
4. Install all the dependencies. Run `pip install -r requirements.txt`
5. Setup role and database in postgres.
    * Run `sudo -u postgres psql`
    * Create role and database `\i create.sql;`
    * To close postgres `\q`
6. Run the `export FLASK_APP=app.py` in terminal.
7. Run the `flask db upgrade` in project terminal to create tables.
8. Run both the command for dummy data `flask dummyuser` and `flask dummypost`.
9. Run the `flask run` in terminal.
10. For clean up role and database.
    * Run `sudo -u postgres psql`
    * Drop role and database `\i drop.sql;`
    * To close postgres `\q`

## About Project
Hello Seller and Buyer, we make this website to provide an ease for you in property dealing. We are here to help you to build a connection between seller and buyer in a very efficient way. Our vision is to remove the brokerage amount which is taking from the seller and buyer by broker. In this website you can easly connect with seller and get the info about any property.