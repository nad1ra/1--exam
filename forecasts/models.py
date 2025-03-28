from django.db import models
from locations.models import Location


class Forecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='forecasts')
    forecast_date = models.DateField()
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    humidity = models.FloatField()
    precipitation_probability = models.FloatField()
    wind_spend = models.FloatField()
    wind_direction = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Forecast for {self.location.name if self.location else 'Unknown Location'} on {self.forecast_date}"

