from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^login/$', auth_views.login, name='registration/login'),
    url(r'^logout/$', auth_views.logout, name='logout'),	
    url(r'^$', views.index, name='index'),
    url(r'^casos/$',views.casos, name="casos"),
    url(r'^caso/$', views.casoFormulario, name="casoFormulario")
]
