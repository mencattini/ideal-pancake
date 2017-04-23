from stew.core import Sort, generator

from ADT.types.bool import Bool
from ADT.types.nat import Nat
from ADT.types.char import Char
from ADT.types.string import String
from ADT.types.relative import Z
from ADT.types.relative_list import List
from ADT.types.map import Map


class Expr(Sort):
    """ Expr sort wraps all python data types considered """

    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and isinstance(args[0], Sort):
            arg = args[0]

            # to avoid multiple if switch
            d = {
                "Bool": Expr.expr_bool,
                "Nat": Expr.expr_nat,
                "Char": Expr.expr_char,
                "String": Expr.expr_string,
                "Z": Expr.expr_z,
                "List": Expr.expr_z_list,
                "Map": Expr.expr_map,
            }

            self._generator = d[arg.__class__.__name__]
            self._generator_args = {'expr': arg}
        else:
            Sort.__init__(self, **kwargs)

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

    def __str__(self):
        return '%s[%s]' % ("E", self._generator_args['expr'])
