from . import views
from django.urls import path

urlpatterns = [
    path('', views.director_list_api_view),
    path('<int:id>/', views.dir_detail_api_view),
    path('movies/', views.movie_list_api_view),
    path('movies/<int:id>/', views.movie_detail_api_view),
    path('reviews/', views.review_list_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
    path('movies/reviews/', views.MovieListView.as_view()),
]