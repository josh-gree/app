import sys
sys.path.insert(0, "..")

from app.app import means

def test_app1():
    out = means('tests/data.csv')
    assert out == {'bob':4.0,'steve':4.0,'will':8.0}

def test_app2():
    out = means('data.csv')
    assert out == None
