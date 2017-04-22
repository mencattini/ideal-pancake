from stew.core import Sort, generator

from ADT.types.nat import Nat
from ADT.types.expr_list import Expr_list


class Char(Sort):

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], str):
            letter = args[0]

            Sort.__init__(self)
            self._generator = Char.char
            self._generator_args = {'value': Nat(ord(letter))}
        else:
            Sort.__init__(self, **kwargs)

    @generator
    def char(value: Nat) -> Char:
        pass

    # Possibility to call a function in a Char term
    @generator
    def func(e_list: Expr_list) -> Char:
        pass

    def _as_char(self):
        return chr(self._generator_args['value']._as_int())

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self._as_char())
