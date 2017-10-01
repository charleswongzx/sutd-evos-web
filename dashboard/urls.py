from django.conf.urls import include, url
from .views import MainDashboard
from .views import *





urlpatterns = [
    # # url(r'^$', MainDashboard.as_view(), name='maindash'),
    # url(r'^$', include(router.urls), name='dashboard'),
]

print(router.urls)




