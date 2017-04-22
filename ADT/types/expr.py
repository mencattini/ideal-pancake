from stew.core import Sort, generator

from ADT.types.bool import Bool
from ADT.types.nat import Nat
from ADT.types.char import Char
from ADT.types.string import String
from ADT.types.relative import Z
from ADT.types.relative_list import List
from ADT.types.map import Map


class Expr(Sort):
    ''' Expr sort wraps all python data types considered '''

    @generator
    def expr_bool(expr: Bool) -> Expr:
        pass

    @generator
    def expr_nat(expr: Nat) -> Expr:
        pass

    @generator
    def expr_char(expr: Char) -> Expr:
        pass

    @generator
    def expr_string(expr: String) -> Expr:
        pass

    @generator
    def expr_z(expr: Z) -> Expr:
        pass

    @generator
    def expr_z_list(expr: List) -> Expr:
        pass

    @generator
    def expr_map(expr: Map) -> Expr:
        pass
