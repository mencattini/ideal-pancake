import ast

a = """

@app.route('/adding')
def adding():
    nickname = request.args.get('nickname')
    text = request.args.get('text')
    if text and nickname:
        future = [persist_post(nickname, text) for text in wrap(text, 140)]
        loop = asyncio.new_event_loop()
        loop.run_until_complete(asyncio.wait(future))
    return redirect(url_for('index'))

async def persist_post(nickname, text):
    post = models.Post(nickname=nickname, text=text)
    await asyncio.sleep(1)
    db.session.add(post)
    db.session.commit()

"""
tree = ast.parse(a)
print(ast.dump(tree))
