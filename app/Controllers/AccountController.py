from flask import request
from flask_restful import Resource
from Models.Account import AccountModel

class AccountController(Resource):
    def get(self):
        args = request.args
        balance = AccountModel.query.filter_by(id=args.get('account_id')).first()
        if not balance:
            return 0 ,404, {'Content-Type':'application/json'}
        return balance.balance
    