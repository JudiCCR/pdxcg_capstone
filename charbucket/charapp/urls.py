from django.urls import path
from . import views

app_name = 'charapp'
urlpatterns = [
    path('', views.userhome, name='userhome'),
    path('nu_post/', views.nu_post, name='nu_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
]