from funct import is_true

def test_z_is_true():
    assert is_true(True) == True

def test_z_is_not_true():
    assert is_true(False) == False
    assert is_true(0) == False
    assert is_true("") == False
    assert is_true(None) == False
