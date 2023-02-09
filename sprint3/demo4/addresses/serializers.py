from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(max_length=127)
    number = serializers.IntegerField()
