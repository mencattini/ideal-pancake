from adt.util.expr_list import Expr_list
from adt.util.expr import Expr
from adt.util.literal import Literal

from adt.types.nat import Nat
from adt.types.string import String

expr1 = Expr.expr_lit(Literal.lit_nat(Nat(2)))
expr2 = Expr.expr_variable(String("test"))
u_expr_list = Expr_list.cons(tail=Expr_list.empty(), head=expr2)
expr_list = Expr_list.cons(tail=u_expr_list, head=expr1)

def test_car():
    assert Expr_list.car(expr_list) == expr1

def test_cdr():
    assert Expr_list.cdr(expr_list) == u_expr_list
    assert Expr_list.car(Expr_list.cdr(expr_list)) == expr2
