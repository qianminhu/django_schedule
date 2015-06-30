from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add', views.add, name='add')
#     todo: remove url add.html maybe
]