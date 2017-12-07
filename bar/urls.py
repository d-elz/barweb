
from django.conf.urls import url , include
from . import views


urlpatterns = [

    #Main menu guide
    url(r'^$', views.index , name='index'  ),
    url(r'^register/$', views.register , name='register'  ),
    url(r'^about/$', views.about , name='about'  ),
    url(r'^contact/$', views.contact , name='contact'  ),
    url(r'^active/$', views.active_users , name='active_users'  ),
    url(r'^public/$', views.public_users , name='public_users'  ),
    url(r'^exchange/$', views.exchange_keys , name='exchange_keys'  ),

    #Bulletin Board
    url(r'^exchange_client/$', views.exchange_client , name='exchange_client'  ),
    url(r'^active_client/$', views.active_client , name='active_client'  ),
    url(r'^public_client/$', views.public_client , name='public_client'  ),

    # For Log in
    url(r'^login/$', views.login , name='login'  ),
    url(r'^auth/$', views.auth_view , name='auth_view'  ),
    url(r'^logout/$', views.logout , name='logout'  ),


]
