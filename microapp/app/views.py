from app import app, models, db
from flask import render_template, request, redirect, url_for
import asyncio


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.all()
    return render_template('index.html', title='MicroBlog', posts=posts)


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
