from django.urls import path

from . import views


app_name = 'poll'


urlpatterns = [
    path('votes/<int:poll_id>/', views.vote, name='vote'),
    path('polls/<int:poll_id>/', views.poll_view, name='poll_view'),
    path('result/<int:poll_id>/', views.result, name='result'),
]
