from app import app, models, db
from flask import render_template, request, redirect, url_for

import asyncio


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.all()
    tri = request.args.get('tri')
    if tri is not None:
        loop = asyncio.new_event_loop()
        res = loop.run_until_complete(tri_by_name(posts))
        loop.close()
        return render_template('index.html', title='MicroBlog', posts=res, tri=True)
    return render_template('index.html', title='MicroBlog', posts=posts, tri=False)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/adding')
def adding():
    nickname = request.args.get('nickname')[0:64]
    text = request.args.get('text')[0:140]
    if text != "" and nickname != "":
        post = models.Post(nickname=nickname, text=text)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/clean')
def clean():
    db.session.query(models.Post).delete()
    db.session.commit()
    return redirect(url_for('index'))


async def tri_by_name(posts):
    return sorted(posts, key=lambda post: post.nickname)
