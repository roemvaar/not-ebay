from django.conf.urls import url, include
from django.contrib import admin
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
