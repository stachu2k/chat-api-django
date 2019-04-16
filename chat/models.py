from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'room'

class Message(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_utc_timestamp = models.BigIntegerField()
    room = models.ForeignKey('Room', related_name='messages', on_delete=models.CASCADE)

    class Meta:
        db_table = 'message'
