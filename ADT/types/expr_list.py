from stew.core import Sort, generator, operation
from collections.abc import Sequence
from ADT.types.expr import Expr
from stew.matching import var


class Expr_list(Sort):
    """ Expr_list sort is a list of expressions intended to represent the effective parameters in a function call"""

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], Sequence):

            if len(args[0]) == 0:
                self._generator = Expr_list.empty
            else:
                self._generator = Expr_list.cons
                self._generator_args = {'tail': Expr_list(args[0][:-1]), 'head': Expr(args[0][-1])}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Expr_list:
        pass

    @generator
    def cons(tail: Expr_list, head: Expr) -> Expr_list:
        pass

    @operation
    def car(e_list: Expr_list) -> Expr:
        if e_list == Expr_list.cons(tail=var.tail, head=var.head):
            return var.head
        else:
            return Expr.empty()

    @operation
    def cdr(e_list: Expr_list) -> Expr_list:
        if e_list == Expr_list.cons(tail=var.tail, head=var.head):
            return var.tail
        else:
            return Expr_list.empty()

    def _as_list(self):
        if self._generator == Expr_list.empty:
            return ''
        elif self._generator == Expr_list.cons:
            if self._generator_args['tail']._generator == Expr_list.empty:
                return self._generator_args['head'].__str__()
            return self._generator_args['tail']._as_list() + ',' + self._generator_args['head'].__str__()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_list())
