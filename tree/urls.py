from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tree_index'),
    path('login/', views.login_user, name='tree_login'),
    path('logout/', views.logout_user, name='tree_logout'),
]