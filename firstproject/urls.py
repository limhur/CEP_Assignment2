from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from notes.models import Note
from notes.views import NoteDelete


urlpatterns = patterns('',
    url(r'^listall/$', ListView.as_view(model=Note), name='listall'),

    url(r'^note/(?P<note_id>\d+)$', views.note, name='detail'),
    url(r'^tag/(?P<tags>.*)$', views.notes_tags, name='notes_list'),
    url(r'^list/(?P<folder>.*)$', views.notes_list, name='notes_list'),
    url(r'^add/$', views.NoteCreate.as_view(), name='note_add'),
    url(r'^note/(?P<pk>\d+)/edit/$', views.NoteUpdate.as_view(),  name='note_update'),
    url(r'^detail/(?P<pk>\d+)$', DetailView.as_view(model=Note), name='detail'),
    url(r'^note/(?P<pk>\d+)/delete/$', NoteDelete.as_view(model=Note), name='delete'),
   
    #url(r'^note/(?P<note_id>\d+)$', views.note, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
