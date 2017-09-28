from django.conf.urls import include, url
from django.contrib import admin

from dashing.utils import router

from dashboard.widgets import NewClientsWidget

router.register(NewClientsWidget, 'test_widget')

urlpatterns = [
    url(r'^test', include(router.urls)),  # main dashboard
    url(r'^admin/', include(admin.site.urls)),  # admin page
    url(r'^logger/', include('logger.urls')),  # log viewer placeholder
    url(r'^$', include('dashboard.urls')),
]
