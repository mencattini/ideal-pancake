from stew.core import Sort, generator, operation
from stew.matching import var
from collections.abc import Sequence


class List(Sort):

    def __init__(self, *args, **kwargs):
        if(len(args) == 1) and isinstance(args[0], Sequence):
            Sort.__init__(self)

            if len(args[0]) == 0:
                self._generator = List.empty
            else:
                self._generator = List.cons
                self._generator_args = {'tail': List(args[0][:-1]), 'head': args[0][-1]}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> List:
        pass

    @generator
    def cons(tail: List, head: Sort) -> List:
        pass

    @operation
    def __add__(tail: List, head: List) -> List:
        # x + [] = x
        if head == List.empty():
            return tail
        # [] + y = y
        if tail == List.empty():
            return head
        #  x + (y,c) = cons(x + y, c)
        if head == List.cons(tail=var.y, head=var.c):
            return List.cons(tail=tail + var.y, head=var.c)
