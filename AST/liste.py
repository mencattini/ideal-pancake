from stew.core import Sort, generator, operation
from stew.matching import var
from collections.abc import Sequence


class Liste(Sort):

    def __init__(self, *args, **kwargs):
        if(len(args) == 1) and isinstance(args[0], Sequence):
            Sort.__init__(self)

            if len(args[0]) == 0:
                self._generator = Liste.empty
            else:
                self._generator = Liste.add
                self._generator_args = {'self': Liste(args[0][:-1]), 'other': args[0][-1]}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def empty() -> Liste:
        pass

    @generator
    def add(self: Liste, other: Sort) -> Liste:
        pass

    @operation
    def append(self: Liste, other: Liste) -> Liste:
        # x + [] = x
        if other == Liste.empty():
            return self

        #  x + (y,c) = add(x + y, c)
        if other == Liste.add(var.y, var.c):
            return Liste.add(self.append(var.y), var.c)
