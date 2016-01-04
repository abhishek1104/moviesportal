from django.conf.urls import url
from . import views #Import views from same directory!

urlpattern = [
    url(r'^$',views.IndexView.as_view(), name='Index')


]