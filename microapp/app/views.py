from app import app, models, db
from flask import render_template, request, redirect, url_for
import asyncio
from random import randint


@app.route('/')
@app.route('/index')
def index():
    comptes = models.Compte.query.all()
    return render_template('index.html', title='MicroCompte', comptes=comptes, tri=False)


@app.route('/creating')
def creating():
    nickname = request.args.get('nickname')
    if nickname:
        nickname = nickname[0:64]
        account = models.Compte(nickname=nickname, account=0)
        db.session.add(account)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/add')
def add():
    return render_template('add.html')


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


@app.route('/clean')
def clean():
    db.session.query(models.Compte).delete()
    db.session.commit()
    return redirect(url_for('index'))


async def persist_operation(nickname, operation):
    account = models.Compte.query.filter_by(nickname=nickname).first()
    await asyncio.sleep(randint(0, 1))
    if account:
        if "+" in operation:
            account.account += int(operation.strip('+'))
        if "-" in operation:
            account.account -= int(operation.strip('-'))
        if account.account < 0:
            print("\n\nAccount smaller than zeros\n\n")
        db.session.commit()
