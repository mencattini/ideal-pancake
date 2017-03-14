from app import app, models, db
from flask import render_template, request, redirect, url_for


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
    post = models.Post(nickname=nickname, text=text)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))
