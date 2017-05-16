from stew.core import Sort, Attribute, generator, operation
from stew.matching import var

from ADT.types.literal import Literal
from ADT.types.expr import Expr
from ADT.types.unary_op import Unary_op
from ADT.types.binary_op import Binary_op
from ADT.types.funct_list import String_list, Func_list, Func
from ADT.types.block import Block
from ADT.types.context import Context
from ADT.types.instr import Instr
from ADT.types.bool import Bool


class Prog(Sort):
    """Prog sort represents the whole program state with the related list of contexts, list of functions and block of instructions"""

    context = Attribute(domain = Context)
    func_list = Attribute(domain = Func_list)
    block = Attribute(domain = Block)

    @operation
    def eval_instr(prog: Prog) -> Prog:
        
        # assign statement
        if car(prog.block) == Instr.assign(var.name, var.expr):
            literal = Expr.eval_expr(var.expr)
            return prog.where(
                    context = add(prog.context, var.name, literal),
                    func_list = prog.func_list,
                    block = cdr(prog.block))

        # if statement
        if car(prog.block) == Instr.if(var.cond, var.b_then, var.b_else):
            bool_literal = Expr.eval_expr(var.cond)
            if bool_literal == Bool.true():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = Block.concat(Block.cdr(prog.block), var.b_then))
            if bool_literal == Bool.false():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = Block.concat(Block.cdr(prog.block), var.b_else))

        # while statement
        if car(prog.block) == Instr.while(var.cond, var.block):
            bool_literal = eval_expr(var.cond)
            if bool_literal == Bool.true():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = Block.concat(prog.block, var.block))
            if bool_literal == Bool.false():
                return prog.where(
                        context = prog.context,
                        func_list = prog.func_list,
                        block = cdr(prog.block))

        # expr statement
        if car(prog.block) == Inst.expr(var.expr):
            Expr.eval_expr(var.expr)
            return prog.where(
                    context = prog.context,
                    func_list = prog.func_list,
                    block = cdr(prog.block))
        pass

        

    @operation
    def eval_expr(expr: Expr, context: Context) -> Literal:

        # literal
        if expr == Expr.expr_num(var.num):
            return var.num

        # variable
        if expr == Expr.expr_variable(var.var_name):
            lit = Context.get_value(context, var_name)
            return lit

        # unary operations
        if expr == Expr.expr_unary(var.op, var.expr):
            lit = Expr.eval_expr(var.expr, context)

            # not
            if var.op == Unary_op.not():
                lit = Literal.lit_bool(var.bool)
                return Literal.lit_bool(Bool.not(var.bool))

            # uSub
            if var.op == Unary_op.uSub():
                lit = Literal.lit_z(var.literal)
                return Literal.lit_z(__sub__(zero(), var.literal))
            pass

        # binary operations
        if expr == Expr.expr_binary(var.op, var.expr1, var.expr2):
            lit1 = Expr.eval_expr(var.expr1, context)
            lit2 = Expr.eval_expr(var.expr2, context)

            # add
            if var.op == Binary_op.add():
                lit1 = Literal.lit_z(var.literal1)
                lit2 = Literal.lit_z(var.literal2)
                return Literal.lit_z(__add__(var.literal1, var.literal2))

            # sub
            if var.op == Binary_op.sub():
                lit1 = Literal.lit_z(var.literal1)
                lit2 = Literal.lit_z(var.literal2)
                return Literal.lit_z(__sub__(var.literal1, var.literal2))

            # mult
            if var.op == Binary_op.mult():
                lit1 = Literal.lit_z(var.literal1)
                lit2 = Literal.lit_z(var.literal2)
                return Literal.lit_z(__mult__(var.literal1, var.literal2))

            # div
            if var.op == Binary_op.div():
                lit1 = Literal.lit_z(var.literal1)
                lit2 = Literal.lit_z(var.literal2)
                return Literal.lit_z(__div__(var.literal1, var.literal2))

            # modulo
            if var.op == Binary_op.modulo(): 
                lit1 = Literal.lit_z(var.literal1)
                lit2 = Literal.lit_z(var.literal2)
                return Literal.lit_z(__mod__(var.literal1, var.literal2))

            # and
            if var.op == Binary_op.and():
                lit1 = Literal.lit_bool(var.literal1)
                lit2 = Literal.lit_bool(var.literal2)
                return Literal.lit_bool(__and__(var.literal1, var.literal2))

            # or
            if var.op == Binary_op.or():
                lit1 = Literal.lit_bool(var.literal1)
                lit2 = Literal.lit_bool(var.literal2)
                return Literal.lit_bool(__or__(var.literal1, var.literal2))

            # xor
            if var.op == Binary_op.xor():
                lit1 = Literal.lit_bool(var.literal1)
                lit2 = Literal.lit_bool(var.literal2)
                return Literal.lit_bool(__xor__(var.literal1, var.literal2))
            pass

    def __str__(self):
        return '%s[%s]' % ("E", self._generator_args['expr'])











