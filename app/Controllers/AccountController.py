from flask import Response, make_response, request
from flask_restful import Resource
from Models.Account import AccountModel

class AccountController(Resource):
    def get(self):
        args = request.args
        balance = AccountModel.query.filter_by(id=args.get('account_id')).first()
        if not balance:
            return make_response(Response('0') ,404)
        return balance.balance
    