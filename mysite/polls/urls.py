from django.urls import path

from .views import index, openpage, BBLoginView, profile, BBLogoutView, RegisterDoneView, RegisterUserView


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', openpage, name='other'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),


]

