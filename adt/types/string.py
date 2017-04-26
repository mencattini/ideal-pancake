from adt.types.char import Char
from stew.core import Sort, generator, operation
from collections.abc import Sequence
from stew.matching import var


class String(Sort):
    def __init__(self, *args, **kwargs):
        if(len(args) == 1) and isinstance(args[0], Sequence):
            Sort.__init__(self)

            if len(args[0]) == 0:
                self._generator = String.empty
            else:
                self._generator = String.cons
                self._generator_args = {'tail': String(args[0][:-1]), 'head': Char((args[0][-1]))}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> String:
        pass

    @generator
    def cons(tail: String, head: Char) -> String:
        pass

    @operation
    def __add__(tail: String, head: String) -> String:
        # x + [] = x
        if head == String.empty():
            return tail
        # [] + y = y
        if tail == String.empty():
            return head
        #  x + (y,c) = cons(x + y, c)
        if head == String.cons(tail=var.y, head=var.c):
            return String.cons(tail=tail + var.y, head=var.c)

    @operation
    def pop(tail: String) -> String:
        if tail == String.cons(tail=var.tail, head=var.head):
            return var.tail, var.head
        else:
            return String.empty(), String.empty()

    def _as_list(self):
        if self._generator == String.empty:
            return ''
        elif self._generator == String.cons:
            if self._generator_args['tail'] == String.empty():
                return str(self._generator_args['head']._as_char())
            else:
                return self._generator_args['tail']._as_list() + self._generator_args['head']._as_char()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_list())
