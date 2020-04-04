import json
from flask import request
from flask_restful import Resource
from flask_expects_json import expects_json
from app.models import db, Ongs
from app.controllers.validators import ong_login


class SessionController(Resource):

    @expects_json(schema=ong_login)
    def post(self):
        ong_id = request.get_json()['id']
        ong = Ongs.query.filter_by(id=ong_id).first()

        if not ong:
            return {
                "error": "No ONG found with this ID"
            }, 400

        return {'name': ong.name}
