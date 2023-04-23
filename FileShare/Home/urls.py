from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view,name='home'),
    path('handle/',views.HandleFileUpload.as_view()),
    path('download/<uid>', views.download_view,name='download'),
]