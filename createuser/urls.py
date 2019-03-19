from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'registration/$', SnippetList.as_view()),
url(r'getvalues/$', Getvalues.as_view()),
url(r'deleterecords/$', Deleterecord.as_view()),
url(r'getuser/$', Getuser.as_view()),
url(r'updateuser/$', Updateuser.as_view())


]
