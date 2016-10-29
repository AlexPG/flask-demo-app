from demo_app import db

entry_category = db.Table('entry_category',
    db.Column('id_entry', db.Integer, db.ForeignKey('entry.id')),
    db.Column('id_category', db.Integer, db.ForeignKey('category.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    email = db.Column(db.String(120), unique=True)

    entry = db.relationship('Entry', backref=db.backref('authors'))

    def __init__(self, name, description, email):
        self.name = name
        self.description = description
        self.email = email

    def __repr__(self):
        return self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    ca_en = db.relationship('Entry', secondary=entry_category)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('entries', cascade='all, delete-orphan'))

    en_ca = db.relationship('Category', secondary=entry_category, \
                            backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def __repr__(self):
        return self.title

    def refresh_categories(self):
        self.en_ca = []
