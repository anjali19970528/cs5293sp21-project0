import pytest

def test_fetchincidents(url):
         assert project0.fetchincidents(url) is not None

def test_extract_fields():
    byte_data=project0.fetchincidents(url)
    str_data=project0.extractincidents(byte_data)
    assert str_data is not None
    for i in str_data:
        assert len(i) == 5

