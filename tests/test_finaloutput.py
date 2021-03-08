import pytest
import sqlite3
def test_status():
    db=sqlite3.connect('normanpd.db')
    a = list(db.execute("SELECT `nature`, count(*) FROM `incidents`  GROUP BY `nature`" ))
#     print(a[0])
    assert a[0] == ('911 Call Nature Unknown', 3)
