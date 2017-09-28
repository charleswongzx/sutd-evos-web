from django.db import models


class EngineStatus(models.Model):
    timestamp = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    rpm = models.IntegerField(default=0)
    pressure = models.FloatField(default=0)
    fuel_flow = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Engine Statuses"

    def __str__(self):
        return 'Status' + str(self.timestamp)


# class AccessoryStatus(models.Model):
#     signal_left = models.BooleanField()
#     signal_right = models.BooleanField()
#     hazard = models.BooleanField()
#     headlights = models.BooleanField()
#     wiper = models.BooleanField()
#     showoff = models.IntegerField()
