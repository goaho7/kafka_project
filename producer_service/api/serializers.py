from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=500)
