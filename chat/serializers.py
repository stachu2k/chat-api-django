# pylint: disable=no-member

import time
from rest_framework import serializers
from chat.models import Room, Message

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')

class MessageSerializer(serializers.ModelSerializer):
    created = TimestampField()
    class Meta:
        model = Message
        fields = ('id', 'text', 'author', 'created', 'room')
