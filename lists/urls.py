from django.conf.urls import url
from lists import views

app_name = "lists"
urlpatterns = [
	url(r'^$', views.home_page, name='home'),
	url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list')
]