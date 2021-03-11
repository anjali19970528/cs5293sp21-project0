# cs5293sp21-project0

Name: Anjali Reddy Tippana

Project descripiton:
In this project, I'm going to download a pdf of the daily incident summary from the norman police report webpage - https://www.normanok.gov/public-safety/police-department/crime-prevention-data/daily-activity-reports and generate a summary of the incident nature along with their count.

How to run:
To run the code first you need to intsall and setup python3 environment with packages mentioned in pipfile or requirements.txt

Commands used to install packages:
pipenv install PyPDF2
pipenv install db-sqlite3
pipenv install re
  
command used to run:
pipenv run python project0/main.py --incidents <url>

Example : pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf 

main.py in project0 folder is going to take a url given in the command and run the code.

How to test:
pipenv run pytest or pipenv run python -m pyest.

Assumptions:
I'm assuming that every time I run the code by paasing url new database is created.

How to develop a database:
First we should import sqlite3, it creates a sqlite database with given name and establishes a connection with the created database. After creation it will return database instance. Using the returned database instance we can run CURD(create,update,read,delete) operations.  

Table creation:
create_statement="""CREATE TABLE IF NOT EXISTS incidents (
                        incident_time TEXT,
                        incident_number TEXT,
                        incident_location TEXT,
                        nature TEXT,
                        incident_ori TEXT
                        )"""
						
Insertion:
db.execute("INSERT INTO incidents (incident_time, incident_number, incident_location, nature,incident_ori)"
                      " VALUES (?, ?, ?, ?, ?)", (incidents[i][0], incidents[i][1], incidents[i][2], incidents[i][3], incidents[i][4]))

After establishing db connection, using above sql statements I created incidents table in normanpd.db database and inserted values using the functions createdb(),populatedb() respectively.					  

Functions used:
fetchincidents(url): This function will take a url in the form of string from the norman police report webpage and returns incident data summary in the byte form.

extractincidents(incident_data): This function is going to take data in byte form and return a list of rows(each row has 1 each date_time, incident number, incident location, nature, and incident ori).

createdb(): This function creates a sqlite database named as normanpd.db and returns a db instance.

populatedb(db, incidents): This function is going to take normanpd.db database instance and list of rows of incident summary and create a table in database with columns incident_time, incident_number, incident_location, 
nature, incident_ori respectively.

status(db): This function is going to take normanpd.db database instance and generate natures of incidents summary along with their count.
