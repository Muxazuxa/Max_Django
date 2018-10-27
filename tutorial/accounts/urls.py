from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html')),
    url(r'^register/$', views.register, name='register')
]