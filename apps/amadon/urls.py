from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout),
    url(r'^buy/(?P<product_id>[0-9]+)$', views.buy),
    url(r'^reset$', views.reset)
]