from app import db


class Compte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True)
    account = db.Column(db.Integer, index=True)

    def __repr__(self):
        return 'Compte'\
            + str(self.id) + ') from : '\
            + self.nickname + '\n\t'\
            + self.account
