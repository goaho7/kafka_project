import json

from api.serializers import MessageSerializer
from kafka import KafkaProducer
from rest_framework.response import Response
from rest_framework.views import APIView


class ProducerView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        producer = KafkaProducer(
            bootstrap_servers="kafka:9093", value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        producer.send("my_topic", serializer.validated_data)
        producer.flush()
        return Response({"status": "Message sent to Kafka"})
