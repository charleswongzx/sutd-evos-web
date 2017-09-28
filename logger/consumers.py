from channels import Group
from .models import EngineStatus
import json


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('vehicle').add(message.reply_channel)


def ws_disconnect(message):
    Group('vehicle').discard(message.reply_channel)


def ws_message(message):

    obj = json.loads(message.content['text'])
    print(obj)

    # Mirrors message back to sender
    message.reply_channel.send({
        'text': message.content['text']
    })

    timestamp = obj['timestamp']
    speed = obj['speed']
    temp = obj['temp']
    # pressure = obj['pressure']
    # rpm = obj['rpm']
    # fuel_flow = obj['fuel_flow']

    status = EngineStatus(
        timestamp=timestamp,
        speed=speed,
        temperature=temp)
    #pressure=pressure, rpm=rpm, fuel_flow=fuel_flow
    status.save()
    # print(status.id)
