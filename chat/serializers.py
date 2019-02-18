# pylint: disable=no-member

from rest_framework import serializers
from chat.models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'messages')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'text', 'author', 'created', 'room')
