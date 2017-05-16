import ast


class Traductor(ast.NodeVisitor):

    def __init__(self):
        # we store the built prog
        self.prog = ""
        self.line = []

    def visit_Module(self, node):
        """Visit the module body

        Iterate over all ast element in a module
        """
        for ele in node.body:
            tmp = self.visit(ele)
            if tmp:
                self.prog += tmp + "\n"
                self.line.append(ele.lineno)

    def visit_FunctionDef(self, node):
        # first we store the name of func
        s = "Func(String(%s), " % (node.name)
        s += "[%s], " % (", ".join([ele.arg for ele in node.args.args]))
        s += 'Expr_list([%s]))' % (
            ", ".join([self.visit(ele) for ele in node.body])
            )
        return s

    def visit_AsyncFunctionDef(self, node):
        # first we store the name of func
        s = "AsyncFunc(String(%s), " % (node.name)
        s += "[%s], " % (", ".join([ele.arg for ele in node.args.args]))
        s += 'Expr_list([%s]))' % (
            ", ".join([self.visit(ele) for ele in node.body])
            )
        return s

    def visit_If(self, node):
        # first we add the Boolean comparing
        s = "If(Bool(%s), " % (self.visit(node.test))
        s += "Expr_list(["
        # then we iterate over the expression in the then
        s += ", ".join([self.visit(ele) for ele in node.body])
        s += "]), Exrp_list(["
        # then we iterate over the expression in the else
        s += ", ".join([self.visit(ele) for ele in node.orelse])
        s += "]))"
        return s

    def visit_While(self, node):
        # first we add the Booleancomparing
        s = "While(Bool(%s), " % (self.visit(node.test))

        s += "Expr_list(["
        # then we ireate over the expression in the body
        s += ", ".join([self.visit(ele) for ele in node.body])
        s += "]))"
        return s

    def visit_Return(self, node):
        return 'Return(%s)' % (self.visit(node.value))

    def visit_Assign(self, node):
        """Give us assign
        """
        s = "Assign("
        # we get the targets, we suppose that we always have
        # only on target
        s += self.visit(node.targets[0]) + ","
        # we get the value
        s += self.visit(node.value) + ")"
        return s

    def visit_Dict(self, node):
        # we suppose that the dictionnary is alwasy "string" -> "expr"
        s = 'Context({'
        # we iterate and construct the couple key/value
        for index, _ in enumerate(node.keys):
            if index == len(node.keys) - 1:
                s += '%s:%s' % (
                    self.visit(node.keys[index]),
                    self.visit(node.values[index])
                    )
            else:
                s += '%s:%s, ' % (
                    self.visit(node.keys[index]),
                    self.visit(node.values[index])
                    )
        s += "})"
        return s

    def visit_List(self, node):
        # iterate over the value and store expr in the list
        values = ", ".join([self.visit(ele) for ele in node.elts])
        return 'Expr_list([%s])' % (values)

    def visit_Compare(self, node):
        s = '%s ' % (self.visit(node.left))
        # we suppose we have only on comparaison
        s += self.visit(node.ops[0]) + " "
        s += self.visit(node.comparators[0])
        return s

    def visit_Call(self, node):
        s = 'Call(%s, %s)' % (
            self.visit(node.func),
            ", ".join([self.visit(arg) for arg in node.args])
            )
        return s

    def visit_Expr(self, node):
        """Give us the value of an expression
        """
        return 'Expr(%s)' % (self.visit(node.value))

    def visit_Await(self, node):
        return 'Await(%s)' % (self.visit(node.value))

    def visit_BinOp(self, node):
        s = ""
        # we get the left, right operand, and the operator
        s += self.visit(node.left)
        s += self.visit(node.op)
        s += self.visit(node.right)
        return s

    def visit_UnaryOp(self, node):
        return self.visit(node.op) + self.visit(node.operand)

    def visit_USub(self, node):
        return "-"

    def visit_UAdd(self, node):
        return "+"

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

    def visit_NotEq(self, node):
        return "!="

    def visit_Div(self, node):
        return " / "

    def visit_Sub(self, node):
        return " - "

    def visit_Add(self, node):
        return " + "

    def visit_Name(self, node):
        return 'String(%s)' % (str(node.id))

    def visit_Str(self, node):
        return 'String(%s)' % (str(node.s))

    def visit_Num(self, node):
        return 'Z(%s)' % (str(node.n))


def print_prog(program, line):
    print("\n")
    for [expr, no] in zip(program.split('\n'), line):
        print(no, ".\t", expr)
    print("\n")


if __name__ == '__main__':
    s = """

t = [1,2,3,4]
s = 5
s = s + 5
s = 5 - 1
10 / 5
d = {'a': 5, 'b': 4}
a = 5
if s > a:
    s = 0 + d
    "Hello World"
else:
    s=1
while s < 10:
    s = s + 1

def my_func(a,b,c):
    res = a + b
    res = res / c
    return res

async def func(a, b, c):
    res = a + b
    await res / c
    return res

func(1, 2, 3)
        """
    t = ast.parse(s)
    # print(s)
    # print(ast.dump(t))
    x = Traductor()
    x.visit(t)
    print_prog(s, list(range(len(s))))
    print_prog(x.prog, x.line)
