from stew.core import Sort, generator, operation
from stew.matching import var

from adt.types.instr import Instr


class Block(Sort):
    """Block sort is the list of instructions representing the programm to be executed"""

    @generator
    def empty() -> Block:
        pass

    @generator
    def cons(tail: Block, head: Instr) -> Block:
        pass

    @operation
    def car(block: Block) -> Instr:
        if block == Block.cons(var.t, var.h):
            return var.h
        # No precision about car(Empty)
        pass

    @operation
    def cdr(block: Block) -> Block:
        if block == Block.cons(var.t, var.h):
            return var.t
        # No precision about cdr(Empty)
        pass
