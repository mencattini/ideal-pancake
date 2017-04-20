from ADT.types.char import Char
from ADT.types.nat import Nat


def test_generator():
    assert Char.char(Nat(10))._generator == Char.char


def test_constructor():
    assert Char('a') == Char.char(Nat(97))


def test_str_():
    assert Char('a').__str__() == 'Char(a)'
