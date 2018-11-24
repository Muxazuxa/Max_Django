from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy, resolve


app_name="accounts"

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', auth_views.PasswordResetView.as_view(
        template_name='accounts/reset_password.html',
        success_url = reverse_lazy('accounts:password_reset_done'),
        email_template_name ='accounts/reset_password_email.html'),
        {'email_template_name':'accounts/reset_password_email.html'},
        name='password_reset'),
    url(r'^reset-password/done/$', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/reset_password_confirm.html',
        success_url = reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name = 'password_reset_complete')
]