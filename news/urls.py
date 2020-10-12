
from django.conf.urls import url
from . import views


urlpatterns = [
url('', views.api_index),
#url(r'<int:pk>', views.NewsDetail.as_view()),
]
