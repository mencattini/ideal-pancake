import ast


class Traductor(ast.NodeVisitor):

    def __init__(self):
        self.stack = 0

    def generic_visit(self, node):
        self.stack += 2
        print(self.stack * ' ', type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
        self.stack -= 2

    def visit_Assign(self, node):
        print(self.stack * ' ', node.__class__.__name__)
        self.stack += 2
        ast.NodeVisitor.generic_visit(self, node)
        self.stack -= 2

    def visit_Name(self, node):
        print(
            self.stack * ' ', node.__class__.__name__,
            '= (%s)' % (str(node.id)))

    def visit_Num(self, node):
        print(
            self.stack * ' ', node.__class__.__name__,
            '= (%s)' % (str(node.n)))


if __name__ == '__main__':
    s = """s = 5;s = s + 5;"""
    t = ast.parse(s)
    print(ast.dump(t))
    x = Traductor()
    x.visit(t)
