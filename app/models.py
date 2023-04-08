from app import db

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    num_ord = db.Column(db.Integer)
    cost_s = db.Column(db.Float)
    date = db.Column(db.String(32))#, default=datetime.utcnow)
    cost_r = db.Column(db.Float)

    def __repr__(self):
        return '<Order {}>'.format(self.num_ord)
