    
from django.conf.urls import url
from django.urls import path, include

from .views import MovieList, MovieDetail, MovieCreation, MovieUpdate, MovieDelete
from .views import PersonList, PersonDetail, PersonCreation, PersonUpdate, PersonDelete
urlpatterns = [   
    url(r'^$', MovieList.as_view(), name='list'),
    
    url(r'^movies/$', MovieList.as_view(), name='list'),
    url(r'^movie/(?P<pk>\d+)$', MovieDetail.as_view(), name='detail'),
    url(r'^movie/new$', MovieCreation.as_view(), name='new'),
    url(r'^movie/edit/(?P<pk>\d+)$', MovieUpdate.as_view(), name='edit'),
    url(r'^movie/delete/(?P<pk>\d+)$', MovieDelete.as_view(), name='delete'),
    
    url(r'^persons/$', PersonList.as_view(), name='list_p'),
    url(r'^person/(?P<pk>\d+)$', PersonDetail.as_view(), name='detail_p'),
    url(r'^person/new$', PersonCreation.as_view(), name='new_p'),
    url(r'^person/edit/(?P<pk>\d+)$', PersonUpdate.as_view(), name='edit_p'),
    url(r'^person/delete/(?P<pk>\d+)$', PersonDelete.as_view(), name='delete_p'),
    path('accounts/', include('django.contrib.auth.urls')),
]