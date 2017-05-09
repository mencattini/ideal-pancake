import ast


class Traductor(ast.NodeVisitor):

    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node):
        s = 'Assign(String(%s)' % (node.targets[0].id)
        if node.value.__class__.__name__ == 'Num':
            s += ',Z(%s))' % (node.value.n)
            print(s)


if __name__ == '__main__':
    s = """s = 5;s = s + 5;"""
    t = ast.parse(s)
    x = Traductor()
    x.visit(t)
