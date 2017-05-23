from stew.core import Sort, generator, operation
from adt.util.expr import Expr
from stew.matching import var


class Expr_list(Sort):
    """ Expr_list sort is a list of expressions intended to represent the
    effective parameters in a function call"""
    """
    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], Sequence):

            if len(args[0]) == 0:
                self._generator = Expr_list.empty
            else:
                self._generator = Expr_list.cons
                self._generator_args = {
                    'tail': Expr_list(args[0][:-1]),
                    'head': Expr(args[0][-1])}
        else:
            Sort.__init__(self, **kwargs)
    """
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

    @operation
    def cdr(e_list: Expr_list) -> Expr_list:
        if e_list == Expr_list.cons(tail=var.tail, head=var.head):
            return var.tail
    """
    @operation
    def rm_nth(e_list: Expr_list, n: Nat) -> Expr_list:
        return Expr_list._rm_nth(e_list=e_list, n=(e_list.length() - n))

    @operation
    def _rm_nth(e_list: Expr_list, n: Nat) -> Expr_list:
        # if the list is empty, just return empty
        if e_list == Expr_list.empty():
            return Expr_list.empty()
        elif e_list == Expr_list.cons(tail=var.tail, head=var.head):
            # if it's the end, we return the tail
            if n == Nat.zero():
                return var.tail
            # or we construct list and decrease the index
            else:
                return Expr_list.cons(
                    tail=var.tail._rm_nth(n - Nat(1)),
                    head=var.head)

    @operation
    def length(e_list: Expr_list) -> Nat:
        if e_list.equality(Expr_list.empty()):
            return Nat(0)
        elif e_list == Expr_list.cons(tail=var.tail, head=var.head):
            if Expr_list.empty().equality(var.tail):
                return Nat(0)
            else:
                return Expr_list.length(var.tail) + Nat(1)

    @operation
    def __add__(tail: Expr_list, head: Expr_list) -> Expr_list:
        # x + [] = x
        if head == Expr_list.empty():
            return tail
        # [] + y = y
        if tail == Expr_list.empty():
            return head
        #  x + (y,c) = cons(x + y, c)
        if head == Expr_list.cons(tail=var.y, head=var.c):
            return Expr_list.cons(tail=tail + var.y, head=var.c)


    def _as_list(self):
        if self._generator == Expr_list.empty:
            return ''
        elif self._generator == Expr_list.cons:
            if self._generator_args['tail']._generator == Expr_list.empty:
                return self._generator_args['head'].__str__()
            return (
                self._generator_args['tail']._as_list() +
                ',' + self._generator_args['head'].__str__())

    def equality(self, other):
        if (
            (self._generator == other._generator)
            and
            self._generator == Expr_list.empty
            ):
            return True
        elif self._generator != other._generator:
            return False
        elif self._generator == other._generator:
            if self._generator_args['head'] == other._generator_args['head']:
                return (
                (self._generator_args['tail']).equality(
                other._generator_args['tail']))
            else:
                return False

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_list())
    """
