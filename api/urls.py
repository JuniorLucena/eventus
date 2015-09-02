from django.conf.urls import include, url
from api import views

urlpatterns = [
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/register/', views.UserCreateView.as_view(), name='user-register'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
]
