from flask import request
from flask_restful import Resource
from app.models import db, Ongs
from secrets import token_hex


class OngController(Resource):

    def get(self):
        ongs = Ongs.query.all()

        return [ong.serialize() for ong in ongs]

    def post(self):
        new_ong = request.get_json()
        new_ong['id'] = token_hex(4)

        db.session.add(Ongs(**new_ong))
        db.session.commit()

        return {"id": new_ong['id']}
