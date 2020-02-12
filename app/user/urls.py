from django.conf.urls import url, include
from . import views

app_name = 'user'
urlpatterns = [
    url(r'create/', views.CreateUserView.as_view(), name='create'),
    url(r'token/', views.CreateTokenView.as_view(), name='token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
