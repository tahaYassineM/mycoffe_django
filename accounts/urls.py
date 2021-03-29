from django.urls import path, include
from . import views

# app_name = 'accounts'

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("oauth/", include("social_django.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('register', views.register_v2, name='register'),
    path('register2', views.register, name='register2'),
    path('profile', views.profile, name='profile'),
]

# urlpatterns = [
#     path("dashboard/", views.dashboard, name="dashboard"),
#     path('signup', views.signup, name='signup'),
#     path('login', login, {'template_name': 'login.html'}, name='login'),
#     path('logout', logout, name='logout'),
#     path('profile', views.profile, name='profile'),
# ]
