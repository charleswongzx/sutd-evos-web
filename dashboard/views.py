from dashing.views import Dashboard
from logger.models import EngineStatus


class MainDashboard(Dashboard):
    stat = EngineStatus.objects
    template_name = 'dashing/dashboard.html'

