import pytest
import os
from os import path
import sqlite3
from project0 import project0

def test_createdb():
    database='normanpd.db'
    d_b=project0.createdb()
    a=path.exists(database)
    assert True == a

def test_populatedb():
    
    db=sqlite3.connect('normanpd.db')
    
    table_values=list(db.execute('SELECT * FROM incidents'))
    assert table_values is not None

