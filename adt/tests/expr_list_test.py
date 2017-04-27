from adt.types.expr_list import Expr, Expr_list
from adt.types.nat import Bool, Nat


def test_generator():
    assert Expr_list.empty()._generator == Expr_list.empty
    assert Expr_list.cons(tail=Expr_list.empty(), head=Expr(Nat(10)))._generator == Expr_list.cons


def test_constructor():
    assert Expr_list.cons(
        tail=Expr_list.cons(
            tail=Expr_list.empty(),
            head=Expr(Nat(1) + Nat(2))
        ),
        head=Expr(Nat(0) > Nat(1))
    ) == Expr_list([Nat(1) + Nat(2), Nat(0) > Nat(1)])

    assert Expr_list.empty() == Expr_list([])


def test_car():
    a = Expr_list([Bool.true(), Nat(10), Nat(11)])
    assert Expr(Nat(11)) == a.car()
    assert Expr.empty() == Expr_list.empty().car()


# def test_cdr():
#     a = Expr_list([Bool.true(), Nat(10), Nat(11)]).cdr()
#     assert Expr_list([Bool.true(), Nat(10)]) == a
#     assert Expr_list.empty() == Expr_list.empty().cdr()
