from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret123'
# Error probably here;
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/bth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Ongs(db.Model):

    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)


class Incidents(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(), nullable=False)
    value = db.Column(db.Float(asdecimal=True), nullable=False)

    ong_id = db.Column(db.String(20), db.ForeignKey('ongs.id'), nullable=False)


if __name__ == "__main__":
    app.run(debug=True)
