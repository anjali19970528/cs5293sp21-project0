import pytest
import os
from os import path
import sqlite3
import os
cwd = os.getcwd()
import sys
sys.path.insert(1,cwd+"/project0/")
import project0

def test_createdb():
    database='normanpd.db'
    d_b=project0.createdb()
    a=path.exists(database)
    assert True == a

def test_populatedb():
    url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf"
    incident_data = project0.fetchincidents(url)
    incidents = project0.extractincidents(incident_data)
    db = project0.createdb()
    project0.populatedb(db, incidents) 
    db=sqlite3.connect('normanpd.db')
    table_values=list(db.execute('SELECT * FROM incidents'))
    assert table_values is not None

