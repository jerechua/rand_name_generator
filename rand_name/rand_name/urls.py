from django.conf.urls import patterns, include, url

from random_name_generator import views as main_views
from random_name_api import views as api_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', main_views.RandNameGeneratorView.as_view(), name='home'),

    #API Views
    url(r'^api/generate/?$', api_views.RandNameGeneratorView.as_view(), name='generate_name'),

)
