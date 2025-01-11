import pytest
from fuel import gauge, convert

def test_str_input():
    with pytest.raises(ValueError):
        convert('cat/cat')

def test_convert():
    assert convert('1/4') == 25

def test_numerador_maior():
    with pytest.raises(ValueError):
        convert('2/1')

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_empty():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_number():
    assert gauge(50) == '50%'
