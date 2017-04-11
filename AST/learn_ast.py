import ast

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
        if account.account < 0:
            print("\n\nAccount smaller than zeros\n\n")
        db.session.commit()

"""
tree = ast.parse(a)
print(ast.dump(tree))
