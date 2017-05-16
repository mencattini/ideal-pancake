from stew.core import Sort, generator

from ADT.types.expr import Expr
from ADT.types.bool import Bool
from ADT.types.string import String
from ADT.types.block import Block


class Instr(Sort):
    """ Instr sort represents an instruction. It may be an assignation, an if or while statement or the call of a function"""

    # Assignation of an expression to a variable
    @generator
    def assign(varName: String, expr: Expr) -> Instr:
        pass

    # If statement
    @generator
    def if(cond: Expr, b_then: Block, b_else: Block) -> Instr:
        pass

    # While statement
    @generator
    def while(cond: Expr, block: Block) -> Instr:
        pass

    # Expression statement
    @generator
    def expr(expr: Expr) -> Instr:
        pass



