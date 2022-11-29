from app import db
from flask import Response
from Models.Account import AccountModel
from Serializers.DepositSerializer import depositSerializer
from Serializers.WithdrawSerializer import withdrawSerializer
from Serializers.TransferSerializer import transferSerializer

def handle(args):
    match args['type']:
        case 'deposit':
            if not (args['amount']): return Response('0'), 400
            if args['amount'] < 0: return Response('0'), 400
            if not args['destination']: return Response('0'), 400
            return deposit(args)
        case 'withdraw':
            if not (args['amount']): return Response('0'), 400
            if args['amount'] < 0: return Response('0'), 400
            if not args['origin']: return Response('0'), 400
            return withdraw(args)
        case 'transfer':
            if not (args['amount']): return Response('0'), 400
            if args['amount'] < 0: return Response('0'), 400
            if not args['destination']: return Response('0'), 400
            if not args['origin']: return Response('0'), 400
            return transfer(args)
        case _:
            return Response('0'), 400
    
def deposit(args):
    account = AccountModel.query.filter_by(id=args['destination']).first()
    if(account):
        account.balance += args['amount']
    else:
        account = AccountModel(id=args['destination'], balance = args['amount'])
        
    db.session.add(account)    
    db.session.commit()
    
    return depositSerializer(account), 201

def withdraw(args):
    account = AccountModel.query.filter_by(id=args['origin']).first()
    if not account: return Response('0'), 404
    
    new_balance = account.balance - args['amount']
    if new_balance < 0: return Response('0'), 406
    account.balance = new_balance;
    
    db.session.commit()
    
    return withdrawSerializer(account), 201

def transfer(args):
    origin = AccountModel.query.filter_by(id=args['origin']).first()
    destination = AccountModel.query.filter_by(id=args['destination']).first()
    if not origin or not destination: return Response('0'), 404
    new_origin_balance = origin.balance - args['amount']
    if new_origin_balance < 0: return Response('0'), 406
    
    origin.balance = new_origin_balance;
    destination.balance += args['amount']
    
    db.session.commit()
    
    return transferSerializer(origin, destination), 201    
