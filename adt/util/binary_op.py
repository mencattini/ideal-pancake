from stew.core import Sort, generator, operation
from sew.matching import var

class Binary_Op(Sort):
    """Operation sort represents a basic python operation taking two arguments"""

    # Here we mix what python call BinOp and BoolOp
    @generator
    def add() -> Binary_op:
        pass

    @generator
    def sub() -> Binary_op:
        pass

    @generator
    def mult() -> Binary_op:
        pass

    @generator
    def div() -> Binary_op:
        pass

    @generator
    def modulo() -> Binary_op:
        pass

    @generator
    def and() -> Binary_op:
        pass

    @generator
    def or() -> Binary_op:
        pass

    @generator
    def xor() -> Binary_op:
        pass
