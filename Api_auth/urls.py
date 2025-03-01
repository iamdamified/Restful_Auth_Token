from django.urls import path
from .views import *


urlpatterns = [
    path('', api_home, name='api_home'),
    path('create/', api_post_create, name='post_create'),
    path('<int:id>/detail/', api_post_detail, name='post_detail'),
    path('<int:id>/update/', api_post_update, name="post_update"),
    path('<int:id>/delete/', api_post_delete, name='post_delete')
]