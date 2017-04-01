from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^send_contact$', views.json_contact, name='send_contact'),
]
