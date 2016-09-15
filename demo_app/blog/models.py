from demo_app import db

entry_category = db.Table('entry_category',
    db.Column('id_entry', db.Integer, db.ForeignKey('entry.id')),
    db.Column('id_category', db.Integer, db.ForeignKey('category.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    entry = db.relationship('Entry', backref=db.backref('authors', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    ca_en = db.relationship('Entry', secondary=entry_category, \
                            backref=db.backref('categories', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    en_ca = db.relationship('Category', secondary=entry_category, \
                            backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id

    def __repr__(self):
        return '<Title %r>' % self.title