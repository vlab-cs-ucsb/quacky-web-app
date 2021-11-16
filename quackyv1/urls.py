from django.urls import path
from . import views

urlpatterns = [
    path('', views.aws, name='aws'),
    path('aws', views.aws, name='aws'),
    path('azure', views.azure, name='azure'),
    path('gcp', views.gcp, name='gcp'),
    path('usage', views.usage, name='usage')
]