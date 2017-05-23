from stew.core import Sort, generator

from adt.util.literal import Literal
from adt.util.unary_op import Unary_op
from adt.util.binary_op import Binary_op

from adt.types.string import String


class Expr(Sort):
    """ Expr sort represents expressions that appear in the instructions """

    @generator
    def expr_lit(lit: Literal) -> Expr:
        pass

    @generator
    def expr_variable(var_name: String) -> Expr:
        pass

    @generator
    def expr_unary(op: Unary_op, expr: Expr) -> Expr:
        pass

    @generator
    def expr_binary(op: Binary_op, expr1: Expr, expr2: Expr) -> Expr:
        pass

