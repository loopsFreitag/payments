from Serializers.DepositSerializer import depositSerializer
from Serializers.WithdrawSerializer import withdrawSerializer

def transferSerializer(origin, destination):
    return {
        **withdrawSerializer(origin), **depositSerializer(destination)
    }
        