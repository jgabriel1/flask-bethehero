import json
from flask import request
from flask_restful import Resource
from app.models import db, Incidents, Ongs

# marshmallow for input validation?


class IncidentController(Resource):

    def get(self):
        count = Incidents.query.count()

        incidents = db.session.query(Incidents, Ongs).\
            join(Ongs).filter(Incidents.ong_id == Ongs.id).\
            paginate(max_per_page=5).items

        # Implement marshmallow for serialization to fix this (too ugly):
        serialized = []
        for result in incidents:
            incident, ong = result
            serialized.append({
                "id": incident.id,
                "title": incident.title,
                "description": incident.description,
                "value": incident.value,
                "ong_id": ong.id,
                "name": ong.name,
                "email": ong.email,
                "whatsapp": ong.whatsapp,
                "city": ong.city,
                "uf": ong.uf
            })

        return serialized

    # Validate
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

    # Validate
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
