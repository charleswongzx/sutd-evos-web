from django.conf.urls import include, url
from django.contrib import admin

from dashing.utils import router

from django.views.generic.base import RedirectView

from dashboard.widgets import SpeedWidget
from dashboard.widgets import TempWidget
from dashboard.widgets import PressureWidget
from dashboard.widgets import RPMWidget
from dashboard.widgets import MileageWidget
from dashboard.widgets import TelemetryWidget

router.register(SpeedWidget, 'speed_widget')
router.register(TempWidget, 'temp_widget')
router.register(PressureWidget, 'pressure_widget')
router.register(RPMWidget, 'rpm_widget')
router.register(MileageWidget, 'mileage_widget')
# router.register(TelemetryWidget, 'telemetry_widget')


urlpatterns = [
    # url(r'^test/', include(router.urls)),  # main dashboard
    url(r'^admin/', include(admin.site.urls)),  # admin page
    url(r'^logger/', include('logger.urls')),  # log viewer placeholder
    url(r'^dashboard/', include(router.urls)),
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index')
]
