from adt.util.context import Context
from adt.util.literal import Literal

from adt.types.string import String
from adt.types.nat import Nat

def test_add():
    context1 = Context.cons(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(0)))
    context12 = Context.cons(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(4)))
    context2 = Context.add(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(0)))
    context3 = Context.add(c=context2, k=String('b'), v=Literal.lit_nat(Nat(4)))
    context4 = Context.add(c=context2, k=String('c'), v=Literal.lit_nat(Nat(4)))
    assert context2 == context1
    assert context3 == context12
    assert context3 != context1
    assert context4 != context1
    assert context4 != context3

def test_get_value():
    context1 = Context.cons(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(0)))
    context2 = Context.add(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(0)))
    context3 = Context.add(c=context2, k=String('b'), v=Literal.lit_nat(Nat(4)))
    context4 = Context.add(c=context2, k=String('c'), v=Literal.lit_nat(Nat(4)))
    assert Context.get_value(c=context1, k=String('b')) == Literal.lit_nat(Nat(0))
    assert Context.get_value(c=context1, k=String('b')) != Literal.lit_nat(Nat(1))
    assert Context.get_value(c=context3, k=String('b')) == Literal.lit_nat(Nat(4))

def test_remove():
    context1 = Context.cons(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(0)))
    context2 = Context.add(c=Context.empty(),k=String('b'), v=Literal.lit_nat(Nat(0)))
    context3 = Context.add(c=context2, k=String('b'), v=Literal.lit_nat(Nat(4)))
    context4 = Context.add(c=context2, k=String('c'), v=Literal.lit_nat(Nat(4)))
    context5 = Context.cons(c=Context.empty(), k=String('c'), v=Literal.lit_nat(Nat(4)))
    assert Context.remove(c=context1, k=String('b')) == Context.empty()
    assert Context.remove(c=context2, k=String('b')) == Context.empty()
    assert Context.remove(c=context4, k=String('b')) == context5
    assert Context.remove(c=context4, k=String('c')) == context2

