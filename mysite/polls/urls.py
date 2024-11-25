from django.urls import path

# from .views import ResultsView
from .views import index
from .views import openpage
from .views import BBLoginView, BBLogoutView, RegisterView


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', openpage, name='other'),
    path('account/login', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

