from stew.core import Sort, generator

from ADT.types.expr import Expr
from ADT.types.bool import Bool
from ADT.types.string import String
from ADT.types.block import Block


class Instr(Sort):
    """ Instr sort represents an instruction. It may be an assignation, an if or while statement or the call of a function"""

    # Assignation of an expression to a variable
    @generator
    def i_assign(varName: String, expr: Expr) -> Instr:
        pass

    # While statement
    @generator
    def i_while(cond: Bool, block: Block) -> Instr:
        pass

    # If statement
    @generator
    def i_if(cond: Bool, b_then: Block, b_else: Block) -> Instr:
        pass

    # Function (procedure) to be executed (we don't care about the returned value if exists)
    @generator
    def i_func(name: String, e_list: Expr_List) -> Instr:
        pass

    # Return statement
    @generator
    def i_return() -> Instr:
        pass

    # Notify that the program exits from a function
    @generator
    def i_end_func() -> Instr:
        pass
