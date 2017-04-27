from ADT.types.expr_list import Expr_list
from ADT.types.expr import Expr
from ADT.types.nat import Bool, Nat


def test_generator():
    assert Expr_list.empty()._generator == Expr_list.empty
    assert Expr_list.cons(tail=Expr_list.empty(), head=Expr(Nat(10)))._generator == Expr_list.cons


def test_constructor():
    res = Expr_list([Nat(1) + Nat(2), Nat(0) > Nat(1)]) == Expr_list.cons(
        tail=Expr_list.cons(
            tail=Expr_list.empty(),
            head=Expr(Nat(1) + Nat(2))
        ),
        head=Expr(Nat(0) > Nat(1))
    )
    assert res == Bool.true()

    res = Expr_list([]) == Expr_list.empty()
    assert res == Bool.true()


def test_car():
    a = Expr_list([Bool.true(), Nat(10), Nat(11)])
    assert Expr(Nat(11)) == a.car()
    assert Expr.empty() == Expr_list.empty().car()


def test_cdr():
    a = Expr_list([Bool.true(), Nat(10), Nat(11)])
    assert Expr_list([Bool.true(), Nat(10)]) == a.cdr()
    assert Expr_list.empty() == Expr_list.empty().cdr()


def test_eq_():
    assert Bool.true() == (Expr_list([Bool.true(), Nat(10), Nat(11)]) == Expr_list([Bool.true(), Nat(10), Nat(11)]))
    assert Bool.true() == (Expr_list([]) == Expr_list.empty())
    assert Bool.false() == (Expr_list([Bool.true(), Nat(10), Nat(11)]) == Expr_list.empty())
