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
1. Create virtual env for project.
2. Install all the dependencies. Run `pip install -r requirements.txt`
3. Run this to open postgres terminal `sudo -u postgres psql`
4. Run **create.sql** file in postgres. Use `\i create.sql;`.
5. Run the `flask db upgrade` in project terminal to create tables.
6. Run the `export FLASK_APP=app.py` in terminal.
7. Run the `flask run` in terminal.
8. For clear up, role and database. Run this `\i drop.sql;` in postgres.

## About Project
Hello Seller and Buyer, we make this website to provide an ease for you in property dealing. We are here to help you to build a connection between seller and buyer in a very efficient way. Our vision is to remove the brokerage amount which is taking from the seller and buyer by broker. In this website you can easly connect with seller and get the info about any property.