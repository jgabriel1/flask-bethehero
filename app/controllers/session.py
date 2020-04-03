import json
from flask import request, Response
from flask_restful import Resource
from app.models import db, Ongs


class SessionController(Resource):

    def post(self):
        ong_id = request.get_json()['id']
        ong = Ongs.query.filter_by(id=ong_id).first()

        if not ong:
            return Response(
                json.dumps({
                    "error": "No ONG found with this ID"
                }),
                status=400,
                mimetype='application/json'
            )

        return {'name': ong.name}
