from stew.core import Sort, Attribute, generator, operation
from stew.matching import var

from ADT.types.expr_list import Expr_list
from ADT.types.funct_list import String_list, Func_list, Func
from ADT.types.block import Block
from ADT.types.context import Context
from ADT.types.instr import Instr
from ADT.types.bool import Bool
# Add the import


class Prog(Sort):
    """Prog sort represents the whole program state with the related list of contexts, list of functions and block of instructions"""

    context = Attribute(domain = Context)
    func_list = Attribute(domain = Func_list)
    block = Attribute(domain = Block)

    @operation
    def fun2cxt(context: Context, s_list: String_list, e_list: Expr_list) -> Context:
        if (s_list == String_list.cons(var.st, var.sh) and e_list == Expr_list.cons(var.et, var.eh)):
            return fun2cxt(Context.add(context, var.sh, var.eh), var.st, var.et)
        pass

    @operation
    def eval_instr(prog: Prog) -> Prog:
        
        # if statement
        if car(prog.block) == Instr.i_if(var.cond, var.b_then, var.b_else):
            if var.cond == Bool.true():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = Block.concat(Block.cdr(prog.block), var.b_then))
            if var.cond == Bool.false():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = Block.concat(Block.cdr(prog.block), var.b_else))
            pass

        # while statement
        if car(prog.block) == Instr.i_while(var.cond, var.block):
            if var.cond == Bool.true():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = Block.concat(prog.block, var.block))
            if var.cond == Bool.false():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = cdr(prog.block))
            pass

        # assign statement
        if car(prog.block) == Instr.i_assign(var.name, var.expr):
            return prog.where(
                    context = add(prog.context, var.name, var.expr),
                    func_list = prog.func_list,
                    block = cdr(prog.block))
        pass

    @operation
    def eval_func(prog: Prog) -> Prog:
        # Function call in condition
        if car(prog.block) == Instr.i_if(var.cond, var.b_then, var.b_else):

        











