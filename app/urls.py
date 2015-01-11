# -*- coding: utf-8 -*
from django.conf import settings
from django.conf.urls import patterns, url


urlpatterns = patterns('',

    # Static resources
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # Info
    url(r'^$', 'app.controllers.info.landing', name="landing"),
    url(r'^authors$', 'app.controllers.info.authors', name="authors"),

    # Authentication
    url(r'^login$', 'app.controllers.auth.login', name='login'),
    url(r'^signup$', 'app.controllers.auth.signup', name='signup'),
    url(r'^logout$', 'app.controllers.auth.logout', name='logout'),
    url(r'^deauth$', 'app.controllers.auth.deauth', name='deauth'),

    # User
    url(r'^profile$', 'app.controllers.user.profile', name='user_profile'),
    url(r'^preferences$', 'app.controllers.user.preferences', name='user_preferences'),

)
