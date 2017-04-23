from stew.core import Sort, generator, operation
from collections.abc import Sequence
from ADT.types.bool import Bool
from ADT.types.context import Context


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
        if c_list._generator == Context_list.cons:
            return c_list._generator_args['head']
        else:
            return Context.empty()

    @operation
    def cdr(c_list: Context_list) -> Context_list:
        if c_list._generator == Context_list.cons:
            return c_list._generator_args['tail']
        else:
            return Context_list.empty()

    @operation
    def __eq__(self: Context_list, other: Context_list) -> Bool:
        # if it's two empty expr list they are equal
        if self._generator == Context_list.empty and other._generator == self._generator:
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
        if self._generator == Context_list.empty:
            return ''
        elif self._generator == Context_list.cons:
            if self._generator_args['tail']._generator == Context_list.empty:
                return self._generator_args['head'].__str__()
            return self._generator_args['tail']._as_list() + ',' + self._generator_args['head'].__str__()

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_list())
