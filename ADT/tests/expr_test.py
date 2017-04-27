from ADT.types.expr import Expr
from ADT.types.string import Char, String
from ADT.types.nat import Bool, Nat
from ADT.types.relative_list import List, Z
from ADT.types.map import Map


def test_generator():
    assert Expr.empty()._generator == Expr.empty
    assert Expr.expr_bool(expr=Bool.true())._generator == Expr.expr_bool
    assert Expr.expr_nat(expr=Nat(10))._generator == Expr.expr_nat
    assert Expr.expr_char(expr=Char('a'))._generator == Expr.expr_char
    assert Expr.expr_string(expr=String('abc'))._generator == Expr.expr_string
    assert Expr.expr_z(expr=Z(109))._generator == Expr.expr_z
    assert Expr.expr_z_list(expr=List.empty())._generator == Expr.expr_z_list
    assert Expr.expr_map(expr=Map.empty())._generator == Expr.expr_map


def test_constructor():
    assert Expr(Bool.true()) == Expr.expr_bool(expr=Bool.true())
    assert Expr(Nat(10)) == Expr.expr_nat(expr=Nat(10))
    assert Expr(Char('a')) == Expr.expr_char(expr=Char('a'))
    assert Expr(String('abc')) == Expr.expr_string(expr=String('abc'))
    assert Expr(Z(109)) == Expr.expr_z(expr=Z(109))
    assert Expr(List.empty()) == Expr.expr_z_list(expr=List.empty())
    assert Expr(Map.empty()) == Expr.expr_map(expr=Map.empty())
