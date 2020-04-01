from . import app
from app.models import *
from flask import request, jsonify
from secrets import token_hex

# OngController:
@app.route('/ongs', methods=['GET'])
def index():
    with db.engine.connect() as connection:
        ongs = connection.execute('SELECT * FROM ongs')
        return jsonify(ongs)


@app.route('/ongs', methods=['POST'])
def create():
    new_ong = request.get_json()
    new_id = token_hex(4)
    new_ong['id'] = new_id

    pls_add = Ongs(**new_ong)

    db.session.add(pls_add)
    db.session.commit()

    return jsonify({"id": new_id})
