from stew.core import Sort, generator, operation
from collections.abc import Sequence
from ADT.types.expr import Expr
from ADT.types.bool import Bool


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
        if e_list._generator == Expr_list.cons:
            return e_list._generator_args['head']
        else:
            return Expr_list.empty()

    @operation
    def cdr(e_list: Expr_list) -> Expr_list:
        if e_list._generator == Expr_list.cons:
            return e_list._generator_args['tail']
        else:
            return Expr_list.empty()

    @operation
    def __eq__(self: Expr_list, other: Expr_list) -> Bool:
        # if it's two empty expr list they are equal
        if self._generator == Expr_list.empty and other._generator == self._generator:
            return Bool.true()
        # if a generator is empty and the other is cons
        elif not(self._generator == other._generator):
            return Bool.false()
        # if the generators are equal we continue
        elif self._generator_args['head'] == other._generator_args['head']:
            return self._generator_args['tail'].__eq__(other._generator_args['tail'])
        # else we stop
        else:
            return Bool.false()

    def _as_list(self):
        if self._generator == Expr_list.empty:
            return ''
        elif self._generator == Expr_list.cons:
            if self._generator_args['tail']._generator == Expr_list.empty:
                return self._generator_args['head'].__str__()
            return self._generator_args['tail']._as_list() + ',' + self._generator_args['head'].__str__()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_list())
