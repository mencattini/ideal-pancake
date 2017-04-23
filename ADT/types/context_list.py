from stew.core import Sort, generator, operation
from stew.matching import var

from ADT.types.context import Context


class Context_list(Sort):
    """ Context_list sort represents the stack of contexts"""

    @generator
    def empty() -> Context_list:
        pass

    @generator
    def cons(tail: Context_list, head: Context) -> Context_list:
        pass

    @operation
    def car(c_list: Context_list) -> Context:
        if c_list == Context_list.cons(var.t, var.h):
            return var.h
        # No precision about car(Empty)
        pass

    @operation
    def cdr(c_list: Context_list) -> Context_list:
        if c_list == Context_list.cons(var.t, var.h):
            return var.t
        # No precision about cdr(Empty)
        pass
