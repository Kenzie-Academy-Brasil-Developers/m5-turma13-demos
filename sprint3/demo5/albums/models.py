from django.db import models
from datetime import timedelta


class Album(models.Model):
    class Meta:
        db_table = "albums"

    name = models.CharField(max_length=127)
    year = models.PositiveSmallIntegerField()
    serial_number = models.IntegerField(unique=True)

    def total_album_duration(self):
        total = sum([song.duration for song in self.songs.all()], timedelta())

        return total

    def __repr__(self) -> str:
        return f"<Album [{self.id}] - {self.name}>"
