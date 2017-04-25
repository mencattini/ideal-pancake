from stew.core import Sort, generator, operation
from collections.abc import Sequence
from ADT.types.bool import Bool
from ADT.types.context import Context
from stew.matching import var


class Context_list(Sort):
    """ Context_list sort represents the stack of contexts"""

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], Sequence):
            Sort.__init__(self)

            if len(args[0]) == 0:
                self._generator = Context_list.empty
            else:
                self._generator = Context_list.cons
                self._generator_args = {'tail': Context_list(args[0][:-1]), 'head': args[0][-1]}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Context_list:
        pass

    @generator
    def cons(tail: Context_list, head: Context) -> Context_list:
        pass

    @operation
    def car(c_list: Context_list) -> Context:
        if c_list == Context_list.cons(tail=var.tail, head=var.head):
            return var.head
        else:
            return Context.empty()

    @operation
    def cdr(c_list: Context_list) -> Context_list:
        if c_list == Context_list.cons(tail=var.tail, head=var.head):
            return var.tail
        else:
            return Context_list.empty()

    def _as_list(self):
        if self._generator == Context_list.empty:
            return ''
        elif self._generator == Context_list.cons:
            if self._generator_args['tail']._generator == Context_list.empty:
                return self._generator_args['head'].__str__()
            return self._generator_args['tail']._as_list() + ',' + self._generator_args['head'].__str__()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_list())
