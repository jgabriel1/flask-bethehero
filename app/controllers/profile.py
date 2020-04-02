from flask import request
from flask_restful import Resource
from app.models import Incidents


class ProfileController(Resource):

    def get(self):
        ong_id = request.headers['Authorization']
        incidents = Incidents.query.filter_by(ong_id=ong_id).all()

        return [incident.serialize() for incident in incidents]
