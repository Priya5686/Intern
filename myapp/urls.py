from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='myapp/login.html')),
    url(r'^logout/$', LogoutView.as_view(template_name='myapp/logout.html')),
    url(r'^register/$', views.register, name='register')
]





