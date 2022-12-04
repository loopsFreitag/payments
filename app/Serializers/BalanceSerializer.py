def balanceSerialize(account_object):
    return {
        "id": str(account_object.id),
        "balance": account_object.balance
    }
