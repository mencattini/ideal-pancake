from stew.core import Sort, generator, operation
from stew.matching import var

from ADT.types.instr import Instr


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
    
    @operation
    def last(block: Block) -> Instr:
        if Block.cdr(block) == Block.empty():
            return Block.car(block)
        return Block.last(Block.cdr(block))

    @operation
    def pop_end(block: Block) -> Block:
        if Block.cdr(block) == Block.empty():
            return Block.empty()
        return Block.cons(Block.car(block), pop_end(Block.cdr(block)))

    @operation
    def concat(tail: Block, head: Block) -> Block:
        if head == Block.empty():
            return tail
        return Block.concat(Block.cons(Block.last(head), tail), Block.pop_end(head))

