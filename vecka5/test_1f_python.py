from function3 import is_valid_w

def test_valied_values():
    assert is_valid_w(32) == True
    assert is_valid_w(64) == True
    assert is_valid_w(128) == True

def test_invalid_values():
    assert is_valid_w(2) == False
    assert is_valid_w(1) == False
