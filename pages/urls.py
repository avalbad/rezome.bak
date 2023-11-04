from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePageViews.as_view(),name="home")
]