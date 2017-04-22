from stew.core import Sort, generator, operation

from ADT.types.expr_list import Expr_list

class Bool(Sort):

    @generator
    def true() -> Bool: 
        pass

    @generator
    def false() -> Bool: 
        pass

    # Possibility to call a function in a Bool term
    @generator
    def func(e_list: Expr_list) -> Bool:
        pass

    @operation
    def __invert__(self: Bool) -> Bool:
        if self == Bool.true():
            return Bool.false()
        return Bool.true()

    @operation
    def __and__(self: Bool, other: Bool) -> Bool:
        if (self == Bool.true()) and (other == Bool.true()):
            return Bool.true()
        return Bool.false()

    @operation
    def __or__(self: Bool, other: Bool) -> Bool:
        if self == Bool.true():
            return Bool.true()
        if other == Bool.true():
            return Bool.true()
        return Bool.false()

    @operation
    def __xor__(self: Bool, other: Bool) -> Bool:
        if (self == Bool.true()) and (other == Bool.false()):
            return Bool.true()
        if (self == Bool.false()) and (other == Bool.true()):
            return Bool.true()
        return Bool.false()

    def __bool__(self):
        return self == Bool.true()
