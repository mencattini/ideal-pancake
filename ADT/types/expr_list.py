from stew.core import Sort, generator, operation

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
        if e_list == Expr_list.cons(tail=tail, head=head):
            return head
        # No precision about car(empty)

    @operation
    def cdr(e_list: Expr_list) -> Expr_list:
        if e_list == Expr_list.cons(tail=tail, head=head):
            return tail
        # No precision about cdr(empty)
