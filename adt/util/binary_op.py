from stew.core import Sort, generator


class Binary_op(Sort):
    """Operation sort represents a basic python
    operation taking two arguments"""

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
    def o_and() -> Binary_op:
        pass

    @generator
    def o_or() -> Binary_op:
        pass

    @generator
    def xor() -> Binary_op:
        pass
