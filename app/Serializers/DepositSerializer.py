from Serializers.BalanceSerializer import balanceSerialize

def depositSerializer(account_object):
    return {
        "destination": balanceSerialize(account_object)
    }