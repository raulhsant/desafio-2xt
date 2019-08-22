from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.search, name='search'),
    path('purchase', views.purchase, name='purchase'),
    path('list', views.list_quotations, name='list')
]