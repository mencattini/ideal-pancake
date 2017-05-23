import ast

type_to_not_show = (ast.Call, ast.Load, ast.Store)
args_to_not_show = ('left', 'right', 'annotation', 'ctx', 'keywords', 'kwonlyargs', 'vararg', 'kw_defaults', 'kwarg')


def str_node(node):
    if isinstance(node, ast.AST):
        fields = [(name, str_node(val)) for name, val in ast.iter_fields(node) if name not in (args_to_not_show)]
        rv = '%s(%s' % (node.__class__.__name__, ', '.join('%s=%s' % field for field in fields))
        return rv + ')'
    else:
        return repr(node)


def ast_visit(node, level=0):
    print('  ' * level + str_node(node))
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST) and not(isinstance(item, type_to_not_show)):
                    ast_visit(item, level=level + 1)
        elif isinstance(value, ast.AST) and not(isinstance(value, type_to_not_show)):
            ast_visit(value, level=level + 1)


if __name__ == '__main__':
    a = """

if a==3:
    b = 2
    c = 4
else:
    e = 4
"""
    tree = ast.parse(a)

    ast_visit(tree, 0)
