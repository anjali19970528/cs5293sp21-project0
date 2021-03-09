import pytest
import sqlite3
from project0 import project0

def test_status():
    url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf"
    incident_data = project0.fetchincidents(url)
    incidents = project0.extractincidents(incident_data)
    db = project0.createdb()
    project0.populatedb(db, incidents)
    a = list(db.execute("SELECT `nature`, count(*) FROM `incidents`  GROUP BY `nature`" ))
    assert a[0] == ('911 Call Nature Unknown', 3)
