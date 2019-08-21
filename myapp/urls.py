from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.search, name='search'),
    path('buy', views.buy, name='buy'),
    path('list', views.list_quotations, name='list')
]