from django.conf.urls import include, url
from django.contrib import admin
from find.views import register, user_login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register),
    url(r'^login/$', user_login),
]
