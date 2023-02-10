from django.urls import path
from . import views

# from songs.views import SongAlbumView
from songs import views as songs_view

urlpatterns = [
    path("albums/", views.AlbumView.as_view()),
    path("albums/<int:album_id>/songs/", songs_view.SongAlbumView.as_view()),
]
