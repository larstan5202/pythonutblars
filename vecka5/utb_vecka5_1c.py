# Båda ekvivalensklasseran
def test_short_text():
    assert is_long("") == False
    assert is_long("hej") == False
    assert is_long("1234") == False
def test_long_text():
    assert is_long("hello") == True
    assert is_long("puthon") == True
    assert is_long("abcdef") == True



