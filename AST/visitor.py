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

@app.route('/adding')
def adding():
    nickname = request.args.get('nickname')
    operations = request.args.get('operations').split(',')
    if len(operations) and nickname:
        nickname = nickname[0:64]
        future = [persist_operation(nickname, operation) for operation in operations]
        loop = asyncio.new_event_loop()
        loop.run_until_complete(asyncio.wait(future))
    return redirect(url_for('index'))

async def persist_operation(nickname, operation):
    account = models.Compte.query.filter_by(nickname=nickname).first()
    await asyncio.sleep(0)
    if account:
        if "+" in operation:
            account.account += int(operation.strip('+'))
        if "-" in operation:
            account.account -= int(operation.strip('-'))
        db.session.commit()
    """
    tree = ast.parse(a)

    ast_visit(tree, 0)
