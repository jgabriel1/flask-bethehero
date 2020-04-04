import json
from flask import request
from flask_restful import Resource
from app.models import db, Ongs


class SessionController(Resource):

    # Validate
    def post(self):
        ong_id = request.get_json()['id']
        ong = Ongs.query.filter_by(id=ong_id).first()

        if not ong:
            return {
                "error": "No ONG found with this ID"
            }, 400

        return {'name': ong.name}
