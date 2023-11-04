from django.urls import path
from .import views

urlpatterns = [
    path('registr/',views.SignupViews.as_view(),name='signup'),
]