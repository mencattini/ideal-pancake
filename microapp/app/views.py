from app import app, models, db
from flask import render_template, request, redirect, url_for
import asyncio


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.all()
    return render_template('index.html', title='Nichon', posts=posts)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/adding')
def adding():
    nickname = request.args.get('nickname')
    text = request.args.get('text')
    if text != "" and nickname != "":
        post = models.Post(nickname=nickname, text=text)

        # we create the asyncio loop
        loop = asyncio.new_event_loop()

        # Blocking call which returns when the display_date() coroutine is done
        loop.run_until_complete(persist(post))
        loop.close()
    return redirect(url_for('index'))


@app.route('/clean')
def clean():
    posts = models.Post.query.all()
    loop = asyncio.new_event_loop()
    for post in posts:
        loop.run_until_complete(delete(post))
    loop.close()
    return redirect(url_for('index'))


@asyncio.coroutine
def delete(post):
    db.session.delete(post)
    db.session.commit()


@asyncio.coroutine
def persist(post):
    db.session.add(post)
    db.session.commit()
