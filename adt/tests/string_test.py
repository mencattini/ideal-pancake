from adt.types.string import String
from adt.types.char import Char


def test_generator():
    assert String.empty()._generator == String.empty
    assert String.cons(tail=String.empty(), head=Char('a'))._generator == String.cons


def test_constructor():
    assert String('') == String.empty()
    assert String('ab') == String.cons(
        tail=String.cons(tail=String.empty(), head=Char('a')),
        head=Char('b'))


def test_add_():
    assert String('a') + String('b') == String('ab')
    assert String('a') + String('') == String('a')
    assert String('') + String('a') == String('a')
    assert String('') + String('') == String('')


def test_str_():
    assert String('').__str__() == 'String()'
    assert String.empty().__str__() == 'String()'
    assert String('abc').__str__() == 'String(abc)'


def test_pop():
    assert String('abc').pop() == (String('ab'), Char('c'))
    assert String([]).pop() == (String.empty(), String.empty())
