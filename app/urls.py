'''
Created on Sep 24, 2014

@author: apple
'''
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views
urlpatterns = patterns('',
    url(r'^key/$', views.ApiKeyView.as_view()),
    url(r'^sync_location/$', views.CoordsView.as_view())
#     url(r'^coord/$', views.QuoteView.as_view()),
)

