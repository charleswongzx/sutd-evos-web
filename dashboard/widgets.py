# -*- encoding: utf-8 -*-
from dashing.widgets import NumberWidget
from dashing.widgets import KnobWidget
from dashing.widgets import Widget
from dashing.widgets import GraphWidget
from django.core.cache import cache

import time

# cache.set('timestamp', 50, 30)
# cache.set('speed', 50, 30)
# cache.set('temp', 50, 30)
# cache.set('pressure', 50, 30)
# cache.set('rpm', 50, 30)
# cache.set('fuel_flow', 50, 30)


class BannerWidget(Widget):
    title = 'SUTD EVOS'


class ButtonPanelWidget(Widget):
    title = 'Control Panel'
    detail = 'Control Panel'

    def get_detail(self):
        return self.detail


class FuelGraphWidget(GraphWidget):
    title = 'Fuel Consumption'
    more_info = 'km/l vs time (seconds)'
    start_time = time.time()
    data = [{'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 0},
            ]

    def get_data(self):
        new_consumption = cache.get('fuel_flow')
        self.data.pop(0)
        if new_consumption:
            self.data.append({'x': time.time()-self.start_time, 'y': new_consumption})
        else:
            self.data.append({'x': time.time()-self.start_time, 'y': 0})
        return self.data


class TelemetryGauge(KnobWidget):
    title = ''


class SpeedWidget(TelemetryGauge):
    title = 'Speed'
    speed = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 100,
            'readOnly': True,
            'width': 150,
            'height': 150,
            'fgColor': colour,
            'bgColor': '#999999',
            'thickness': 0.25,
            'inputColor': colour,
            }
    detail = 'km/h'

    def get_value(self):
        new_speed = cache.get('speed')
        if not new_speed:
            self.speed = 0
        else:
            self.speed = new_speed
        # self.update_colour()
        return self.speed

    def update_colour(self):
        if self.speed <= 20:
            self.data['fgColor'] = '#65a163'  # green
        elif 20 < self.speed <= 40:
            self.data['fgColor'] = '#ffeb75'  # yellow
        elif 40 < self.speed <= 50:
            self.data['fgColor'] = 'linear-gradient(to right, #0072ff, #00c6ff);'# /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

                #'#f69e54'  # orange
        else:
            self.data['fgColor'] = '#fb556e'  # red


class TempWidget(TelemetryGauge):
    title = 'Eng. Temp.'
    temp = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 500,
            'readOnly': True,
            'width': 150,
            'height': 150,
            'fgColor': colour,
            'bgColor': '#999999',
            'thickness': 0.25,
            'inputColor': colour
            }
    detail = u'\u2103'

    def get_value(self):
        new_temp = cache.get('temp')
        if not new_temp:
            self.temp = 0
        else:
            self.temp = new_temp
        self.update_colour()
        return self.temp

    def update_colour(self):
        if self.temp <= 20:
            self.data['fgColor'] = '#65a163'  # green
        elif 20 < self.temp <= 40:
            self.data['fgColor'] = '#ffeb75'  # yellow
        elif 40 < self.temp <= 50:
            self.data['fgColor'] = '#f69e54'  # orange
        else:
            self.data['fgColor'] = '#fb556e'  # red


class PressureWidget(TelemetryGauge):
    title = 'Pressure'
    pressure = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 5000,
            'readOnly': True,
            'width': 150,
            'height': 150,
            'fgColor': colour,
            'bgColor': '#999999',
            'thickness': 0.25,
            'inputColor': colour
            }
    detail = 'psi'

    def get_value(self):
        new_pressure = cache.get('pressure')
        if not new_pressure:
            self.pressure = 0
        else:
            self.pressure = new_pressure
        self.update_colour()
        return self.pressure

    def update_colour(self):
        if self.pressure <= 20:
            self.data['fgColor'] = '#65a163'  # green
        elif 20 < self.pressure <= 40:
            self.data['fgColor'] = '#ffeb75'  # yellow
        elif 40 < self.pressure <= 50:
            self.data['fgColor'] = '#f69e54'  # orange
        else:
            self.data['fgColor'] = '#fb556e'  # red


class RPMWidget(TelemetryGauge):
    title = 'RPM'
    theme = 'blue'
    rpm = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 5000,
            'readOnly': True,
            'width': 150,
            'height': 150,
            'fgColor': colour,
            'bgColor': '#999999',
            'thickness': 0.25,
            'inputColor': colour
            }
    detail = 'revs/min'

    def get_theme(self):
        return self.theme

    def get_value(self):
        new_rpm = cache.get('rpm')
        if not new_rpm:
            self.rpm = 0
        else:
            self.rpm = new_rpm
        self.update_colour()
        return self.rpm

    def update_colour(self):
        if self.rpm <= 1000:
            self.data['fgColor'] = '#65a163'  # green
        elif 1000 < self.rpm <= 2000:
            self.data['fgColor'] = '#ffeb75'  # yellow
        elif 2000 < self.rpm <= 3000:
            self.data['fgColor'] = '#f69e54'  # orange
        else:
            self.data['fgColor'] = '#fb556e'  # red


class MileageWidget(TelemetryGauge):
    title = 'Mileage'
    mileage = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 400,
            'readOnly': True,
            'width': 150,
            'height': 150,
            'fgColor': colour,
            'bgColor': '#999999',
            'thickness': 0.25,
            'inputColor': colour
            }
    detail = 'km/l'

    def get_value(self):
        new_mileage = cache.get('fuel_flow')
        if not new_mileage:
            self.mileage = 0
        else:
            self.mileage = new_mileage
        self.update_colour()
        return self.mileage

    def update_colour(self):
        if self.mileage <= 20:
            self.data['fgColor'] = '#fb556e'  # red
        elif 20 < self.mileage <= 40:
            self.data['fgColor'] = '#f69e54'  # orange
        elif 40 < self.mileage <= 50:
            self.data['fgColor'] = '#ffeb75'  # yellow
        else:
            self.data['fgColor'] = '#65a163'  # green


class LapWidget(NumberWidget):
    title = 'Current Lap'
    current_lap = 0

    def get_value(self):
        self.current_lap = cache.get('current_lap')
        return 0

    def get_detail(self):
        return '/10'

