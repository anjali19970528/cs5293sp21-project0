import pytest
import os
cwd = os.getcwd()
import sys
sys.path.insert(1,cwd+"/project0/")
import project0

url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf"
def test_fetchincidents():
         assert project0.fetchincidents(url) is not None


def test_extract_fields():
    byte_data=project0.fetchincidents(url)
    str_data=project0.extractincidents(byte_data)
    assert str_data is not None
    for i in str_data:
        assert len(i) == 5

