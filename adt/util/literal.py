from stew.core import Sort, generator

from adt.types.bool import Bool
from adt.types.nat import Nat
from adt.types.char import Char
from adt.types.string import String
from adt.types.relative import Z
from adt.types.relative_list import List
from adt.types.map import Map


class Literal(Sort):
    """ Expr sort wraps all python data types considered """

    @generator
    def lit_bool(lit: Bool) -> Literal:
        pass

    @generator
    def lit_nat(lit: Nat) -> Literal:
        pass

    @generator
    def lit_char(lit: Char) -> Literal:
        pass

    @generator
    def lit_string(lit: String) -> Literal:
        pass

    @generator
    def lit_z(lit: Z) -> Literal:
        pass

    @generator
    def lit_z_list(lit: List) -> Literal:
        pass

    @generator
    def lit_map(lit: Map) -> Literal:
        pass

    def __str__(self):
        return '%s[%s]' % ("E", self._generator_args['literal'])
