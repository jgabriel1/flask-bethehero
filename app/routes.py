from . import api
from app.controllers.ong import OngController
from app.controllers.profile import ProfileController
from app.controllers.session import SessionController
from app.controllers.incident import IncidentController

api.add_resource(OngController, '/ongs')
api.add_resource(ProfileController, '/profile')
api.add_resource(SessionController, '/sessions')
