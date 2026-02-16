def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32



#Testfall

from pytest import approx

def test_c_to_f():
    assert c_to_f(-300) is None
    assert c_to_f(-273.15) == approx(-459.67)
    assert c_to_f(0) == approx(32)
    assert c_to_f(100) == approx(212)


