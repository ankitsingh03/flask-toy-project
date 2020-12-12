# Flask Toy Project

## Aim
You will implement the requirements which is written in the **USER-STORIES.md**.

## Requirements
1. Internet Browser
2. Internet connection
3. Python Version 3.7+
4. Postgresql
5. List of all the dependencies in **requirements.txt**

## How To Run
- Create virtual env for project.
- Install all the dependencies. Run `pip install -r requirements.txt`
- Run the script called **create.sql** in postgres. Run `\i create.sql`
- Run the `flask db upgrade` in project terminal to create tables.
- Run the `export FLASK_APP=app.py` in terminal.
- Run the `flask run` in terminal.   
- For clean up process. You can run `drop.sql` script.

## About Project
Hello Seller and Buyer, we make this website to provide an ease for you in property dealing. We are here to help you to build a connection between seller and buyer in a very efficient way. Our vision is to remove the brokerage amount which is taking from the seller and buyer by broker. In this website you can easly connect with seller and get the info about any property.