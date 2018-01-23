from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static

from dashing.utils import router

from django.views.generic.base import RedirectView

from dashboard.widgets import SpeedWidget
from dashboard.widgets import TempWidget
from dashboard.widgets import PressureWidget
from dashboard.widgets import RPMWidget
from dashboard.widgets import MileageWidget
from dashboard.widgets import TelemetryGauge
from dashboard.widgets import LapWidget
from dashboard.widgets import BannerWidget
from dashboard.widgets import ButtonPanelWidget
from dashboard.widgets import FuelGraphWidget


router.register(SpeedWidget, 'speed_widget')
router.register(TempWidget, 'temp_widget')
router.register(PressureWidget, 'pressure_widget')
router.register(RPMWidget, 'rpm_widget')
router.register(MileageWidget, 'mileage_widget')
router.register(TelemetryGauge, 'telemetry')
router.register(LapWidget, 'lap_widget')
router.register(BannerWidget, 'banner_widget')
router.register(ButtonPanelWidget, 'button_panel_widget')
router.register(FuelGraphWidget, 'fuel_graph_widget')


urlpatterns = [
    # url(r'^test/', include(router.urls)),  # main dashboard
    url(r'^admin/', include(admin.site.urls)),  # admin page
    url(r'^logger/', include('logger.urls')),  # log viewer placeholder
    url(r'^dashboard/', include(router.urls)),
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index')
]

# url = static('dashboard/static/dashing/widgets')
