from . import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Ongs(db.Model):

    id = db.Column(db.String, primary_key=True, autoincrement=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    whatsapp = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    uf = db.Column(db.String, nullable=False)

    def __init__(self, id, name, email, whatsapp, city, uf):
        self.id = id
        self.name = name
        self.email = email
        self.whatsapp = whatsapp
        self.city = city
        self.uf = uf

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "whatsapp": self.whatsapp,
            "city": self.city,
            "uf": self.uf
        }


class Incidents(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    value = db.Column(db.Float(asdecimal=True), nullable=False)
    ong_id = db.Column(db.String, db.ForeignKey('ongs.id'), nullable=False)

    def __init__(self, title, description, value, ong_id):
        self.title = title
        self.description = description
        self.value = value
        self.ong_id = ong_id

    def serialize(self):
        return {
            "title": self.title,
            "description": self.description,
            "value": self.value,
            "ong_id": self.ong_id,
        }
