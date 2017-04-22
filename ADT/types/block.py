from stew.core import Sort, generator, operation

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
        if block == Block.cons(tail=tail, head=head):
            return head
        # No precision about car(Empty)

    @operation
    def cdr(block: Block) -> Block:
        if block == Block.cons(tail=tail, head=head):
            return tail
        # No precision about cdr(Empty)
