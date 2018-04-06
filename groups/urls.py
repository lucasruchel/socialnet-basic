from django.urls import re_path,path
from . import views

app_name = 'groups'

url_patterns = [
    path('',views.ListGroups.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    re_path('posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    
]
