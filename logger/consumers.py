from channels import Group
from .models import EngineStatus
import json
from django.core.cache import cache

recording = False

# TEST VALUES
cache.set('timestamp', 50, 30)
cache.set('running', False, 30)
cache.set('speed', 50, 30)
cache.set('temp', 250, 30)
cache.set('pressure', 50, 30)
cache.set('rpm', 2210, 30)
cache.set('fuel_flow', 50, 30)


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('vehicle').add(message.reply_channel)


def ws_disconnect(message):
    Group('vehicle').discard(message.reply_channel)


def ws_message(message):
    global recording

    # TODO: handle incoming MJPEG
    # TODO: handle incoming eng toggle boolean

    obj = json.loads(message.content['text'])

    if obj['type'] == 'log_begin':
        recording = True

    elif obj['type'] == 'log_end':
        recording = False

    elif obj['type'] == 'eng_toggle':
        cache.set('eng_toggle', obj['toggle'], None)

    elif obj['type'] == 'lap_count':
        cache.set('current_lap', obj['current_lap'], None)

    elif obj['type'] == 'ax_control':
        cache.set('timestamp', obj['timestamp'], None)
        cache.set('source', obj['source'], None)
        cache.set('wipers', obj['wipers'], None)
        cache.set('headlight', obj['headlight'], None)
        cache.set('horn', obj['horn'], None)
        cache.set('sig_l', obj['sig_l'], None)
        cache.set('sig_r', obj['sig_r'], None)
        cache.set('hazard', obj['hazard'], None)

    elif obj['type'] == 'engine_stat':
        new_timestamp = obj['timestamp']
        new_running = obj['running']
        new_speed = obj['speed']
        new_temp = obj['temp']
        new_pressure = obj['pressure']
        new_rpm = obj['rpm']
        new_fuel_flow = obj['fuel_flow']

        # Send stats to cache
        cache.set('timestamp', new_timestamp, 3)
        cache.set('running', new_running, 3)
        cache.set('speed', new_speed, 3)
        cache.set('temp', new_temp, 3)
        cache.set('pressure', new_pressure, 3)
        cache.set('rpm', new_rpm, 3)
        cache.set('fuel_flow', new_fuel_flow, 3)

        if recording:
            status = EngineStatus(
                timestamp=new_timestamp,
                speed=new_speed,
                temperature=new_temp,
                rpm=new_rpm,
                pressure=new_pressure,
                fuel_flow=new_fuel_flow)
            status.save()



