from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^operation$', views.display_operation, name="display_operation"),
    url(r'^mouvement$', views.display_mouvement, name="display_mouvement"),
    url(r'^add_new$', views.add_operation, name="add_operation"),
]
