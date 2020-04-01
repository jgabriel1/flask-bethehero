from . import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Ongs(db.Model):

    __tablename__ = 'ongs'

    id = db.Column(db.String, primary_key=True, autoincrement=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    whatsapp = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    uf = db.Column(db.String, nullable=False)

    def __init__(self, id, name, email, whatsapp, city, uf):
        self.id = id,
        self.name = name,
        self.email = email,
        self.whatsapp = whatsapp,
        self.city = city,
        self.uf = uf,


class Incidents(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    value = db.Column(db.Float(asdecimal=True), nullable=False)

    ong_id = db.Column(db.String, db.ForeignKey('ongs.id'), nullable=False)
