from app import app, models, db
from flask import render_template, request, redirect, url_for

from textwrap import wrap
import asyncio


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.all()
    tri = request.args.get('tri')
    if tri is not None:
        return render_template('index.html', title='MicroBlog', posts=sorted(posts, key=lambda post: post.nickname), tri=True)
    return render_template('index.html', title='MicroBlog', posts=posts, tri=False)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/adding')
def adding():
    nickname = request.args.get('nickname')
    text = request.args.get('text')
    if text and nickname:
        nickname = nickname[0:64]
        future = [persist_post(nickname, text) for text in wrap(text, 140)]
        loop = asyncio.new_event_loop()
        loop.run_until_complete(asyncio.wait(future))
    return redirect(url_for('index'))


@app.route('/clean')
def clean():
    db.session.query(models.Post).delete()
    db.session.commit()
    return redirect(url_for('index'))


async def persist_post(nickname, text):
    post = models.Post(nickname=nickname, text=text)
    await asyncio.sleep(1)
    db.session.add(post)
    db.session.commit()
