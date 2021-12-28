from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='group_posts')),
    path('admin/', admin.site.urls),
]
