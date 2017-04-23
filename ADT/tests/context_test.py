from ADT.types.context import Context
from ADT.types.string import String
from ADT.types.expr import Expr
from ADT.types.nat import Nat, Bool


def test_generator():
    assert Context.empty()._generator == Context.empty
    assert Context.add(
        my_context=Context.empty(),
        key=String('a'),
        value=Expr(Nat(10)))._generator == Context.add


def test_constructor():
    assert Context({}) == Context.empty()
    assert Context({'a': Nat(0), 'b': Bool.true()}) == Context.add(
        my_context=Context.add(
            my_context=Context.empty(),
            key=String('b'),
            value=Expr(Bool.true())),
        key=String('a'),
        value=Expr(Nat(0)))


def test_get_value():
    assert Context({}).get_value(String('a')) == Expr.empty()
    assert Context({'a': Nat(10)}).get_value(String('a')) == Expr(Nat(10))
    assert Context({'a': Nat(10)}).get_value(String('b')) == Expr.empty()


def test_has():
    assert Context({}).has(String('a')) == Bool.false()
    assert Context({'a': Nat(10)}).has(String('a')) == Bool.true()
    assert Context({'a': Nat(10)}).has(String('b')) == Bool.false()


def test_remove():
    assert Context({}).remove(String('a')) == Context({})
    assert Context({'a': Nat(10)}).remove(String('a')) == Context({})
    assert Context({'a': Nat(10), 'b': Nat(11)}).remove(String('a')) == Context({'b': Nat(11)})
