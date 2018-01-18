# -*- encoding: utf-8 -*-
from dashing.widgets import NumberWidget
from dashing.widgets import KnobWidget
from dashing.widgets import Widget
from django.core.cache import cache

# cache.set('timestamp', 50, 30)
# cache.set('speed', 50, 30)
# cache.set('temp', 50, 30)
# cache.set('pressure', 50, 30)
# cache.set('rpm', 50, 30)
# cache.set('fuel_flow', 50, 30)


# Base telemetry widget based off base widget class
class TelemetryWidget(Widget):
    title = ''
    value = ''
    data = {}
    detail = ''
    more_info = ''
    updated_at = ''

    def get_title(self):
        return self.title

    def get_data(self):
        return self.data

    def get_detail(self):
        return self.detail

    def get_more_info(self):
        return self.more_info

    def get_value(self):
        return self.value

    def get_updated_at(self):
        return self.updated_at

    def get_context(self):
        return {
            'title': self.get_title(),
            'value': self.get_value(),
            'data': self.get_data(),
            'detail': self.get_detail(),
            'moreInfo': self.get_more_info(),
            'updatedAt': self.get_updated_at(),
        }


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
        # self.update_colour()
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


class RPMWidget(KnobWidget):
    title = 'RPM'
    rpm = 0
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
    detail = 'RPM'

    def get_value(self):
        new_rpm = cache.get('rpm')
        if not new_rpm:
            self.rpm = 0
        else:
            self.rpm = new_rpm
        self.update_colour()
        return self.rpm

    def update_colour(self):
        if self.rpm <= 20:
            self.colour = '#65a163'  # green
        elif 20 < self.rpm <= 40:
            self.colour = '#ffeb75'  # yellow
        elif 40 < self.rpm <= 50:
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


class MileageWidget(KnobWidget):
    title = 'Mileage'
    mileage = 0
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
            self.colour = '#fb556e'  # red
        elif 20 < self.mileage <= 40:
            self.colour = '#f69e54'  # orange
        elif 40 < self.mileage <= 50:
            self.colour = '#ffeb75'  # yellow
        else:
            self.colour = '#65a163'  # green

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
