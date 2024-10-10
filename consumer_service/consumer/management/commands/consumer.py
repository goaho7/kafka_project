import json

from consumer.models import Message
from django.core.management.base import BaseCommand
from kafka import KafkaConsumer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        consumer = KafkaConsumer(
            "my_topic",
            bootstrap_servers="kafka:9093",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="my-group",
        )

        for message in consumer:
            data = message.value
            Message.objects.create(**data)
