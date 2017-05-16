import ast


class Traductor(ast.NodeVisitor):

    def __init__(self):
        # we store the built prog
        self.prog = "\n"

    def visit_Module(self, node):
        for ele in node.body:
            tmp = self.visit(ele)
            if tmp:
                self.prog += tmp + "\n"

    def visit_Assign(self, node):
        s = "Assign("
        # we get the targets, we suppose that we always have
        # only on target
        s += self.visit(node.targets[0]) + ","
        # we get the value
        s += self.visit(node.value) + ")"
        return s

    def visit_BinOp(self, node):
        s = ""
        # we get the left, right operand, and the operator
        s += self.visit(node.left)
        s += self.visit(node.op)
        s += self.visit(node.right)
        return s

    def visit_If(self, node):
        # first we add the Boolean comparing
        s = "If(Bool(%s), " % (self.visit(node.test))
        s += "Expr_list(["
        # import ipdb
        # ipdb.set_trace()

        for ele in node.body:
            s += self.visit(ele)
        s += "]), Exrp_list(["
        for ele in node.orelse:
            s += self.visit(ele)
        s += "]))\n"
        self.prog += s

    def visit_Compare(self, node):
        s = '%s ' % (self.visit(node.left))
        # we suppose we have only on comparaison
        s += self.visit(node.ops[0]) + " "
        s += self.visit(node.comparators[0])
        return s

    def visit_Gt(self, node):
        return ">"

    def visit_GtE(self, node):
        return ">="

    def visit_Lt(self, node):
        return "<"

    def visit_LtE(self, node):
        return "<="

    def visit_Eq(self, node):
        return "=="

    def visit_Sub(self, node):
        return " - "

    def visit_Add(self, node):
        return " + "

    def visit_Name(self, node):
        return 'String(%s)' % (str(node.id))

    def visit_Num(self, node):
        return 'Z(%s)' % (str(node.n))


if __name__ == '__main__':
    s = """

s = 5
s = s + 5
s = 5 - 1
a = 5
if s > a:
    s = 0
else:
    s=1
        """
    t = ast.parse(s)
    print(ast.dump(t))
    x = Traductor()
    x.visit(t)
    print(x.prog)
