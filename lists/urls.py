from django.conf.urls import url
from lists import views

app_name = "lists"
urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	url(r'^lists/(.+)/$', views.view_list, name='view_list'),
	url(r'^lists/new$', views.new_list, name='new_list')
]