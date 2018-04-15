from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from tastypie.api import Api
from api.resources import TaskResource
from api import views


v1_api = Api(api_name='v1')
v1_api.register(TaskResource())

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/', include(v1_api.urls)),
    url(r'^$', views.HomePageView.as_view(),name='home'),
    url('add', views.HomePageView.addTask,name='add'),
]
