from channels import Group
from .models import EngineStatus
import json

recording = False


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('vehicle').add(message.reply_channel)


def ws_disconnect(message):
    Group('vehicle').discard(message.reply_channel)


def ws_message(message):
    global recording

    obj = json.loads(message.content['text'])

    # # Mirrors message back to sender
    # message.reply_channel.send({
    #     'text': message.content['text']
    # })

    if obj['type'] == 'log_begin':
        recording = True

    elif obj['type'] == 'log_end':
        recording = False

    elif obj['type'] == 'engine_stat':

        new_timestamp = obj['timestamp']
        new_speed = obj['speed']
        new_temp = obj['temp']
        new_pressure = obj['pressure']
        new_rpm = obj['rpm']
        new_fuel_flow = obj['fuel_flow']

        # TODO: SEND TO DASHBOARD

        if recording:
            status = EngineStatus(
                timestamp=new_timestamp,
                speed=new_speed,
                temperature=new_temp,
                rpm=new_rpm,
                pressure=new_pressure,
                fuel_flow=new_fuel_flow)
            status.save()



