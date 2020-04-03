import json
from flask import request, Response
from flask_restful import Resource
from app.models import db, Incidents


class IncidentController(Resource):

    def get(self):
        # query.paginate() pagination object check docs
        incidents = Incidents.query.all()

        return [incident.serialize() for incident in incidents]

    def post(self):
        new_incident = Incidents(
            **request.get_json(),
            ong_id=request.headers.get('Authorization')
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
            return Response(
                json.dumps({
                    "error": "Operation not permitted!"
                }),
                status=401,
                mimetype='application/json'
            )
        else:
            db.session.delete(incident)
            db.session.commit()

            return Response(
                status=204,
                mimetype='application/json'
            )
