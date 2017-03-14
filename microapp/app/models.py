from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True)
    text = db.Column(db.String(140), index=True)

    def __repr__(self):
        return 'Post('\
            + str(self.id) + ') from : '\
            + self.nickname + '\n\t'\
            + self.text
