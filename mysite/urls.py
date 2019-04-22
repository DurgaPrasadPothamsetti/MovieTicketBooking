from django.conf.urls import url, include
from django.contrib.auth import views
from mysite.core import views as core_views
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(next_page='home'), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^booking/$', core_views.booking, name='booking'),
    url(r'^bookings/$', core_views.bookings, name='bookings'),
    url(r'^confirm/$', core_views.confirm, name='confirm'),
    url(r'^ticket/$', core_views.ticket, name='ticket'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    
    url('^', include('django.contrib.auth.urls')),
]