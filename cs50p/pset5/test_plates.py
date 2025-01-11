from plates import is_valid

def test_length():
    assert is_valid('HELLO') == True
    assert is_valid('HELLOOO') == False
    assert is_valid('H') == False

def test_first_letters():
    assert is_valid('h110') == False
    assert is_valid('3e110') == False
    assert is_valid('he110') == True

def test_numbers():
    assert is_valid('HE0LO') == False
    assert is_valid('HE1LO') == False

def test_zero():
    assert is_valid('he012') == False
    assert is_valid('he123') == True

def test_punctuation():
    assert is_valid('HELLO!') == False
    assert is_valid('HELLO.') == False
