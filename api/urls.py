from django.conf.urls import include, url
from api import views

urlpatterns = [
    url(r'^account/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^account/register/', views.UserCreateView.as_view(), name='account-register'),
    url(r'^account/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='account-detail'),
]
