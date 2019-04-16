# pylint: disable=no-member

import time
import datetime
from rest_framework import serializers
from chat.models import Room, Message

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))

    def to_internal_value(self, value):
        return datetime.datetime.utcfromtimestamp(value)

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')

class MessageSerializer(serializers.ModelSerializer):
    created = serializers.IntegerField(source='created_utc_timestamp')
    class Meta:
        model = Message
        fields = ('id', 'text', 'author', 'created', 'room')
