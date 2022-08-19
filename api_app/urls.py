from django.urls import path
from .views import rentViews

from .views import RegisterAPI
from .views import rentViews
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path('rent/', rentViews.as_view()),
    path('rent/<int:id>', rentViews.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    # path('user/<slug:user_name>', userViews.as_view())
]