# -*- encoding: utf-8 -*-
from dashing.widgets import NumberWidget
from dashing.widgets import KnobWidget
from django.core.cache import cache

# cache.set('timestamp', 50, 30)
# cache.set('speed', 50, 30)
# cache.set('temp', 50, 30)
# cache.set('pressure', 50, 30)
# cache.set('rpm', 50, 30)
# cache.set('fuel_flow', 50, 30)


class SpeedWidget(KnobWidget):
    title = 'Speed'
    speed = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 70,
            'readOnly': True,
            'width': 100,
            'height': 100,
            'fgColor': colour,
            'bgColor': '#d3d3d3',
            'inputColor': colour
            }
    detail = 'km/h'

    def get_value(self):
        new_speed = cache.get('speed')
        if not new_speed:
            self.speed = 0
        else:
            self.speed = new_speed
        self.update_colour()
        return self.speed

    def update_colour(self):
        if self.speed <= 20:
            self.colour = '#65a163'  # green
        elif 20 < self.speed <= 40:
            self.colour = '#ffeb75'  # yellow
        elif 40 < self.speed <= 50:
            self.colour = '#f69e54'  # orange
        else:
            self.colour = '#fb556e'  # red

    def get_data(self):
        data = {'angleArc': 240,
                'angleOffset': -120,
                'displayInput': True,
                'step': 1,
                'min': 0,
                'max': 70,
                'readOnly': True,
                'width': 100,
                'height': 100,
                'fgColor': self.colour,
                'bgColor': '#d3d3d3',
                'inputColor': self.colour,
                'lineCap': 'round',
                'thickness': 0.15,
                # 'font': '"Lato", sans-serif',
                # 'fontWeight': 100,
                }
        return data


class TempWidget(KnobWidget):
    title = 'Temp'
    temp = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 70,
            'readOnly': True,
            'width': 100,
            'height': 100,
            'fgColor': colour,
            'bgColor': '#d3d3d3',
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
        print(new_temp)
        return self.temp

    def update_colour(self):
        if self.temp <= 20:
            self.colour = '#65a163'  # green
        elif 20 < self.temp <= 40:
            self.colour = '#ffeb75'  # yellow
        elif 40 < self.temp <= 50:
            self.colour = '#f69e54'  # orange
        else:
            self.colour = '#fb556e'  # red

    def get_data(self):
        data = {'angleArc': 240,
                'angleOffset': -120,
                'displayInput': True,
                'step': 1,
                'min': 0,
                'max': 70,
                'readOnly': True,
                'width': 100,
                'height': 100,
                'fgColor': self.colour,
                'bgColor': '#d3d3d3',
                'inputColor': self.colour,
                'lineCap': 'round',
                'thickness': 0.15,
                # 'font': '"Lato", sans-serif',
                # 'fontWeight': 100,
                }
        return data


class PressureWidget(KnobWidget):
    title = 'Pressure'
    pressure = 0
    colour = '#FFFFFF'
    data = {'angleArc': 240,
            'angleOffset': -120,
            'displayInput': True,
            'step': 1,
            'min': 0,
            'max': 70,
            'readOnly': True,
            'width': 100,
            'height': 100,
            'fgColor': colour,
            'bgColor': '#d3d3d3',
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
        print(new_pressure)
        return self.pressure

    def update_colour(self):
        if self.pressure <= 20:
            self.colour = '#65a163'  # green
        elif 20 < self.pressure <= 40:
            self.colour = '#ffeb75'  # yellow
        elif 40 < self.pressure <= 50:
            self.colour = '#f69e54'  # orange
        else:
            self.colour = '#fb556e'  # red

    def get_data(self):
        data = {'angleArc': 240,
                'angleOffset': -120,
                'displayInput': True,
                'step': 1,
                'min': 0,
                'max': 70,
                'readOnly': True,
                'width': 100,
                'height': 100,
                'fgColor': self.colour,
                'bgColor': '#d3d3d3',
                'inputColor': self.colour,
                'lineCap': 'round',
                'thickness': 0.15,
                # 'font': '"Lato", sans-serif',
                # 'fontWeight': 100,
                }
        return data
