from django.urls import path
from .views import rentViews
from .views import userViews

urlpatterns = [
    path('rent/', rentViews.as_view()),
    path('user/', userViews.as_view()),
    path('user/<slug:user_name>', userViews.as_view())
]