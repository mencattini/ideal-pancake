from adt.util.prog import Prog
from adt.util.literal import Literal
from adt.util.expr import Expr
from adt.util.unary_op import Unary_op
from adt.util.binary_op import Binary_op
from adt.util.block import Block
from adt.util.context import Context
from adt.util.instr import Instr

from adt.types.bool import Bool
from adt.types.nat import Nat
from adt.types.char import Char
from adt.types.string import String
from adt.types.relative import Z
from adt.types.relative_list import List
from adt.types.map import Map


def test_eval_expr():
    var = String('var')
    lit1 = Literal.lit_nat(Nat(5))
    lit2 = Literal.lit_nat(Nat(3))
    context = Context.cons(c=Context.empty(), k=var, v=lit2)
    expr = Expr.expr_lit(lit1)

    # literal
    assert Prog.eval_expr(expr=expr, context=context) == lit1

    # variable
    assert Prog.eval_expr(expr=Expr.expr_variable(var), context=context) == lit2

    # unary operations
    # o.not
    lit_true = Literal.lit_bool(Bool.true())
    lit_false = Literal.lit_bool(Bool.false())
    op = Unary_op.o_not()
    expr_bool = Expr.expr_unary(op=op, expr=Expr.expr_lit(lit_true))
    assert Prog.eval_expr(expr=expr_bool, context=context) == lit_false
    assert Prog.eval_expr(expr=expr_bool, context=context) != lit_true

    # uSub
    lit_z = Literal.lit_z(Z(2))
    lit_z2 = Literal.lit_z(Z(-2))
    op = Unary_op.uSub()
    expr_z = Expr.expr_unary(op=op, expr=Expr.expr_lit(lit_z))
    assert Prog.eval_expr(expr=expr_z, context=context) == lit_z2


    # binary operations
    # add
    lit_z1 = Literal.lit_z(Z(2))
    lit_z2 = Literal.lit_z(Z(-5))
    lit_z3 = Literal.lit_z(Z(-3))
    op = Binary_op.add()
    expr = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_z1), expr2=Expr.expr_lit(lit_z2))
    assert Prog.eval_expr(expr=expr, context=context) == lit_z3

    # sub
    lit_z3 = Literal.lit_z(Z(7))
    op = Binary_op.sub()
    expr = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_z1), expr2=Expr.expr_lit(lit_z2))
    assert Prog.eval_expr(expr=expr, context=context) == lit_z3

    # mult
    lit_z3 = Literal.lit_z(Z(10))
    op = Binary_op.mult()
    expr = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_z1), expr2=Expr.expr_lit(lit_z2))
    # assert Prog.eval_expr(expr=expr, context=context) == lit_z3

    # div
    lit_z3 = Literal.lit_z(Z(2))
    op = Binary_op.div()
    expr = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_z2), expr2=Expr.expr_lit(lit_z1))
    # assert Prog.eval_expr(expr=expr, context=context) == lit_z3

    # modulo
    lit_z3 = Literal.lit_z(Z(1))
    op = Binary_op.modulo()
    expr = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_z2), expr2=Expr.expr_lit(lit_z1))
    # assert Prog.eval_expr(expr=expr, context=context) == lit_z3

    # and
    op = Binary_op.o_and()
    expr1 = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_true), expr2=Expr.expr_lit(lit_true))
    expr2 = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_false), expr2=Expr.expr_lit(lit_true))
    assert Prog.eval_expr(expr=expr1, context=context) == lit_true
    assert Prog.eval_expr(expr=expr2, context=context) == lit_false
    assert Prog.eval_expr(expr=expr2, context=context) != lit_true

    # or
    op = Binary_op.o_or()
    expr1 = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_false), expr2=Expr.expr_lit(lit_false))
    expr2 = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_false), expr2=Expr.expr_lit(lit_true))
    assert Prog.eval_expr(expr=expr1, context=context) == lit_false
    assert Prog.eval_expr(expr=expr2, context=context) == lit_true
    assert Prog.eval_expr(expr=expr2, context=context) != lit_false

    # xor
    op = Binary_op.xor()
    expr1 = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_true), expr2=Expr.expr_lit(lit_true))
    expr2 = Expr.expr_binary(op=op, expr1=Expr.expr_lit(lit_false), expr2=Expr.expr_lit(lit_true))
    assert Prog.eval_expr(expr=expr1, context=context) == lit_false
    assert Prog.eval_expr(expr=expr2, context=context) == lit_true
    assert Prog.eval_expr(expr=expr2, context=context) != lit_false


















