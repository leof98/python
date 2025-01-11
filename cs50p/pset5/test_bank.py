from bank import value

def test_number():
    assert value('0223') == 100

def test_hello():
    assert value('hello') == 0

def test_h():
    assert value('hooray') == 20

def test_case_senstive():
    assert value('HELLO') == 0
