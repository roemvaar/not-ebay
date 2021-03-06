from django.conf.urls import url
from shop import views


app_name = 'shop'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^sell_item/$', views.sell_item, name='sell_item'),
    url(r'^payment/$', views.payment, name='payment'),
]
