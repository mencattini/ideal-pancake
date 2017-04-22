from stew.core import Sort, generator, operation
from stew.matching import var

from ADT.types.expr import Expr


class Expr_list(Sort):
    """ Expr_list sort is a list of expressions intended to represent the effective parameters in a function call"""

    @generator
    def empty() -> Expr_list:
        pass

    @generator 
    def cons(tail: Expr_list, head: Expr) -> Expr_list:
        pass

    @operation
    def car(e_list: Expr_list) -> Expr:
        if e_list == Expr_list.cons(var.t, var.h):
            return var.h
        # No precision about car(empty)
        pass

    @operation
    def cdr(e_list: Expr_list) -> Expr_list:
        if e_list == Expr_list.cons(var.t, var.h):
            return var.t
        # No precision about cdr(empty)
        pass
