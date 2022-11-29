def balanceSerialize(account_object):
    return {
        "id": account_object.id,
        "balance": account_object.balance
    }
    