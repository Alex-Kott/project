from django.conf.urls import url 

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ask_kosh/$', views.ask_kosh, name='ask_kosh'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^logout/$', views.signout, name='signout'),
	url(r'^hot/$', views.hot, name='hot'),
	url(r'^articles/(?P<n>[0-9]{1,4})/$', views.year, name="year"),
	url(r'^tag/(?P<tag>[0-9]{1,4})/$', views.tag, name="tag"),
	url(r'^question/(?P<question_id>[0-9]{1,4})/$', views.question, name="question"),
	url(r'^settings/$', views.settings, name='settings'),

]