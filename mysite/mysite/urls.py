from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('polls.urls', 'polls')),
    path('admin/', admin.site.urls),

]