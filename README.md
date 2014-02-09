Text Analyzer

A simple web app to analyze text and show words used and their frequency of use.


1. Dependencies

python 2.7,
MySQL,
Tornado python framework,
Packages MySQL-python and torndb


2. Installation

Install the above dependencies


3. Setup

Connect to MySQL as a user that can create databases and users and create a database and user 'text_analyzer'

mysql -u root -p

Create a database named "text_analyzer":

   mysql> CREATE DATABASE text_analyzer;

Allow the user "text_analyzer" to connect with password "text_analyzer":

 mysql> GRANT ALL PRIVILEGES ON text_analyzer.* TO 'text_analyzer'@'localhost' IDENTIFIED BY 'text_analyzer';

Import the provided schema.sqll to create tables in the new database

 mysql --user=text_analyzer --password=text_analyzer --database=text_analyzer < text_analyzer.sql


4. Run the application

cd to the app's directory\n
run chmod a+x application.py\n
run ./application.py\n
open http://localhost:8888/ from your browser\n

