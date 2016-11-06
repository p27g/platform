from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'elections'

urlpatterns = [
                  # /home/
                  url(r'^$', views.home, name='home'),
                  url(r'^hashtags/$', views.hashtags, name='hashtags'),
                  url(r'^retweets/$', views.retweets, name='retweets'),
                  url(r'^popularity/$', views.popularity, name='popularity'),
                  url(r'^location/$', views.location, name='location'),
                  url(r'^analysis/$', views.analysis, name='analysis'),
                  url(r'^home/$', views.home, name='home'),


              ] 
