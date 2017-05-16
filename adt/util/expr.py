from stew.core import Sort, generator

from adt.types.expr_list import Expr_list
from adt.types.literal import Literal
from adt_types.string import String
from adt.types.unary_op import Unary_op
from adt.types.binary_op import Binary_op


class Expr(Sort):
    """ Expr sort represents expressions that appear in the instructions """

    @generator
    def expr_lit(lit: Literal) -> Expr:
        pass

    @generator
    def expr_variable(var_name: String) -> Expr:
        pass

    @generator
    def expr_unary(op: Unary_Op, expr: Expr) -> Expr:
        pass

    @generator
    def expr_binary(op: Binary_Op, expr1: Expr, expr2: Expr) -> Expr:
        pass

    def __str__(self):
        return '%s[%s]' % ("E", self._generator_args['expr'])
