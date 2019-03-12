from django.conf.urls import url
from django.contrib import admin
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout, name='logout')
]
