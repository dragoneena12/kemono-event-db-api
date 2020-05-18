from django.conf.urls import include, url
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^account/$', AuthInfoGetView.as_view()),
    url(r'^account_update/$', AuthInfoUpdateView.as_view()),
    url(r'^account_delete/$', AuthInfoDeleteView.as_view()),
]