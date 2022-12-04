from Serializers.BalanceSerializer import balanceSerialize

def withdrawSerializer(account_object):
    return {
        "origin": balanceSerialize(account_object)
    }
    