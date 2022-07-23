from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('video-download', views.down_view, name='singleDown'),
    path('thumbnail-download', views.thumb_view, name='thumbDown')
]
