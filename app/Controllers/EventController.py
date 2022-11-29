from flask_restful import Resource, reqparse
import Services.EventServices as EventServices

event_args = reqparse.RequestParser()
event_args.add_argument("type", type=str, required=True)
event_args.add_argument("destination", type=int)
event_args.add_argument("amount", type=float)
event_args.add_argument("origin", type=int)

class Event(Resource):
    def post(self):
        args = event_args.parse_args()
        result, response_status = EventServices.handle(args)
        return result, response_status, {'Content-Type':'application/json'}
    