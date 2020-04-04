from flask import request
from flask_restful import Resource
from flask_expects_json import expects_json
from app.models import db, Incidents, Ongs
from app.controllers.validators import create_incident

# marshmallow for input validation?


class IncidentController(Resource):

    def get(self):
        count = Incidents.query.count()

        incidents = db.session.query(Incidents, Ongs).\
            join(Ongs).filter(Incidents.ong_id == Ongs.id).\
            paginate(max_per_page=5).items

        # Maybe implement marshmallow for serialization to fix this (too ugly):
        return [{
            **ong.serialize(),
            **incident.serialize()
        } for incident, ong in incidents]

    @expects_json(schema=create_incident)
    def post(self):
        new_incident = Incidents(
            **request.get_json(),
            ong_id=request.headers['Authorization']
        )

        db.session.add(new_incident)
        db.session.flush()
        id = new_incident.id

        db.session.commit()
        return {"id": id}

    def delete(self, id):
        ong_id = request.headers['Authorization']

        incident = Incidents.query.filter_by(id=id).first()

        if incident.ong_id != ong_id:
            return {
                "error": "Operation not permitted!"
            }, 401
        else:
            db.session.delete(incident)
            db.session.commit()

            return {}, 204
