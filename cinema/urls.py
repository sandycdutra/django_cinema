from django.urls import path
from . import views

app_name = 'cinema';

urlpatterns = [
    path('', views.home, name='movie_list'), #Página principal
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/sessions/<int:session_id>/', views.session_detail, name='session_detail'),
    path('sessions/<int:session_id>/seats/<int:seat_id>/book/', views.book_seat, name='book_seat'),
    path('about/', views.about, name='about')
]
