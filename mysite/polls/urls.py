from django.urls import path

from .views import index
from .views import openpage
from .views import BBLogoutView, RegisterDoneView
from .views import login
from .views import register


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', openpage, name='other'),
    path('account/logout/', BBLogoutView.as_view(), name='logout'),
    path('login/', login, name='login'),  # Имя URL для входа
    path('register/', register, name='register'),
    path('account/register/done/', RegisterDoneView.as_view(), name='register_done'),
]

