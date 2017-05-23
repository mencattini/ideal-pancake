from stew.core import Sort, generator

from adt.util.expr import Expr
from adt.util.block import Block

class Instr(Sort):
    """ Instr sort represents an instruction. It may be an assignation, an if or while statement or the call of a function"""

    # Assignation of an expression to a variable
    @generator
    def i_assign(varName: Expr, expr: Expr) -> Instr:
        pass

    # If statement
    @generator
    def i_if(cond: Expr, b_then: Block , b_else: Block) -> Instr:
        pass

    # While statement
    @generator
    def i_while(cond: Expr, block: Block) -> Instr:
        pass

    # Expression statement
    @generator
    def i_expr(expr: Expr) -> Instr:
        pass
