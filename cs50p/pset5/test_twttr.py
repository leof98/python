def main():
    test_numbers()
    test_uppercase()
    test_symbols()

def test_numbers():
    assert shorten('0223') == '0223'

def test_uppercase():
    assert shorten('BANANA') == 'BNN'
    assert shorten('banana') == 'bnn'
    assert shorten('baNAnA') == 'bNn'

def test_symbols():
    assert shorten('.,?!@#$%') == '.,?!@#$%'
