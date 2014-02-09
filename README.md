### Text Analyzer

A simple web app to analyze text and show words used and their frequency of use.


#### Dependencies

* python 2.7
* MySQL
* Tornado python framework
* Packages MySQL-python and torndb


#### Installation

Install the above dependencies


#### Setup

Connect to MySQL as a user that can create databases and users and create a database and user 'text_analyzer'

mysql -u root -p

Create a database named "text_analyzer":

   mysql> CREATE DATABASE text_analyzer;

Allow the user "text_analyzer" to connect with password "text_analyzer":

 mysql> GRANT ALL PRIVILEGES ON text_analyzer.* TO 'text_analyzer'@'localhost' IDENTIFIED BY 'text_analyzer';

Import the provided schema.sqll to create tables in the new database

 mysql --user=text_analyzer --password=text_analyzer --database=text_analyzer < text_analyzer.sql


#### Run the application

cd to the app's directory

run chmod a+x application.py

run ./application.py

open http://localhost:8888/ from your browser


