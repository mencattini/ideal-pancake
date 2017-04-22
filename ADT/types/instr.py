from stew.core import Sort, generator, operation

from ADT.types.expr import Expr
from ADT.types.bool import Bool
from ADT.types.string import String
from ADT.types.block import Block

''' Instr sort represents an instruction. It may be an assignation, an if or while statement
or the call of a function'''
class Instr(Sort):

    # Assignation of an expression to a variable
    @generator
        def i_assign(varName: String, expr: Expr) -> Instr:
            pass

    
    @generator
        def i_while(cond: Bool, block: Block) -> Instr:
            pass
