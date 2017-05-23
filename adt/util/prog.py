from stew.core import Sort, Attribute, operation
from stew.matching import var

from adt.util.literal import Literal
from adt.util.expr import Expr
from adt.util.unary_op import Unary_op
from adt.util.binary_op import Binary_op
from adt.util.block import Block
from adt.util.context import Context
from adt.util.func_list import Func_list
from adt.util.instr import Instr

from adt.types.bool import Bool
from adt.types.relative import Z


class Prog(Sort):
    """Prog sort represents the whole program state with the
    related list of contexts, list of functions and block of instructions"""

    context = Attribute(domain=Context)
    func_list = Attribute(domain=Func_list)
    block = Attribute(domain=Block)

    @operation
    def eval_instr(prog: Prog) -> Prog:

        # assign statement
        if prog.block.car() == Instr.i_assign(varName=var.name, expr=var.expr):
            literal = Expr.eval_expr(expr=var.expr, context=prog.context)
            return prog.where(
                    context=Context.add(c=prog.context, k=var.name, v=literal),
                    func_list=prog.func_list,
                    bloc=prog.block)

        # if statement
        if prog.block.car() == (
                Instr.i_if(cond=var.cond, b_then=var.b_then, b_else=var.b_else)
                ):
            bool_literal = Expr.eval_expr(expr=var.cond, context=prog.context)
            if bool_literal == Bool.true():
                return prog.where(
                        context=prog.context,
                        func_list=prog.func_list,
                        block=prog.block)
            if bool_literal == Bool.false():
                return prog.where(
                        context=prog.context,
                        func_list=prog.func_list,
                        block=prog.block)

        # while statement
        if prog.block.car() == Instr.i_while(cond=var.cond, block=var.block):
            bool_literal = Prog.eval_expr(expr=var.cond, context=prog.context)
            if bool_literal == Bool.true():
                return prog.where(
                        context=prog.context,
                        func_list=prog.func_list,
                        block=prog.block)
            if bool_literal == Bool.false():
                return prog.where(
                        context=prog.context,
                        func_list=prog.func_list,
                        block=prog.block)

        # expr statement
        if prog.block.car() == Instr.i_expr(var.expr):
            Expr.eval_expr(expr=var.expr, head=prog.context)
            return prog.where(
                    context=prog.context,
                    func_list=prog.func_list,
                    block=prog.block)
        pass

    @operation
    def eval_expr(expr: Expr, context: Context) -> Literal:

        # literal
        if expr == Expr.expr_lit(var.lit):
            return var.lit

        # variable
        if expr == Expr.expr_variable(var.var_name):
            lit = Context.get_value(c=context, k=var.var_name)
            return lit

        # unary operations
        if expr == Expr.expr_unary(op=var.op, expr=var.expr):
            lit = Prog.eval_expr(expr=var.expr, context=context)

            # not
            if ((var.op == Unary_op.o_not()) and
                    (lit == Literal.lit_bool(var.bool))):
                return Literal.lit_bool(~var.bool)

            # uSub
            if ((var.op == Unary_op.uSub()) and
                    (lit == Literal.lit_z(var.literal))):
                return Literal.lit_z((Z(0) - var.literal))
            pass

        # binary operations
        if (expr ==
                Expr.expr_binary(op=var.op, expr1=var.expr1, expr2=var.expr2)):
            lit1 = Prog.eval_expr(expr=var.expr1, context=context)
            lit2 = Prog.eval_expr(expr=var.expr2, context=context)

            # add
            if (
                (var.op == Binary_op.add()) and
                (lit1 == Literal.lit_z(var.literal1)) and
                    (lit2 == Literal.lit_z(var.literal2))):
                return Literal.lit_z(var.literal1 + var.literal2)

            # sub
            if (
                (var.op == Binary_op.sub()) and
                (lit1 == Literal.lit_z(var.literal1)) and
                    (lit2 == Literal.lit_z(var.literal2))):
                return Literal.lit_z(var.literal1 - var.literal2)

            # mult
            if (
                (var.op == Binary_op.mult()) and
                (lit1 == Literal.lit_z(var.literal1)) and
                    (lit2 == Literal.lit_z(var.literal2))):
                return Literal.lit_z(var.literal1 * var.literal2)

            # div
            if (
                (var.op == Binary_op.div()) and
                (lit1 == Literal.lit_z(var.literal1)) and
                    (lit2 == Literal.lit_z(var.literal2))):
                return Literal.lit_z(var.literal1 / var.literal2)

            # modulo
            if (
                (var.op == Binary_op.modulo()) and
                (lit1 == Literal.lit_z(var.literal1)) and
                    (lit2 == Literal.lit_z(var.literal2)))():
                return Literal.lit_z(var.literal1 % var.literal2)

            # and
            if (
                (var.op == Binary_op.o_and()) and
                (lit1 == Literal.lit_bool(var.literal1)) and
                    (lit2 == Literal.lit_bool(var.literal2))):
                return Literal.lit_bool(var.literal1 & var.literal2)

            # or
            if (
                (var.op == Binary_op.o_or()) and
                (lit1 == Literal.lit_bool(var.literal1)) and
                    (lit2 == Literal.lit_bool(var.literal2))):
                return Literal.lit_bool(var.literal1 | var.literal2)

            # xor
            if (
                (var.op == Binary_op.xor()) and
                (lit1 == Literal.lit_bool(var.literal1)) and
                    (lit2 == Literal.lit_bool(var.literal2))):
                return Literal.lit_bool(var.literal1 ^ var.literal2)
            pass
