from django.test import TestCase
from albums.models import Album
import ipdb
from django.db.utils import IntegrityError


class AlbumModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.album_data_1 = {
            "name": "Album 1",
            "year": 2023,
            "serial_number": 12345,
        }

        cls.album_1 = Album.objects.create(**cls.album_data_1)

    def test_create_valid_album(self):
        # self.assertEqual(self.album_1.name, self.album_data_1["name"])
        # ipdb.set_trace()
        self.assertDictContainsSubset(self.album_data_1, self.album_1.__dict__)

    def test_album_name_properties(self):
        expected = 127
        resulted = Album._meta.get_field("name").max_length

        msg = f"Verifique se o tamanho máximo permitido por `name` é {expected}"

        self.assertEqual(expected, resulted, msg)

    def test_album_objects_representation(self):
        expected = f"<Album [{self.album_1.id}] - {self.album_1.name}>"
        result = repr(self.album_1)
        # result = self.album_1.__repr__()

        self.assertEqual(expected, result)

    def test_serial_number_uniqueness(self):
        album_data_2 = {
            "name": "Album 2",
            "year": 1993,
            "serial_number": 12345,
        }

        album_2 = Album(**album_data_2)
        # self.assertRaises(IntegrityError, album_2.save)

        # expected_message = "UNIQUE constraint failed: albums_album.serial_number"
        # ipdb.set_trace()
        expected_message = (
            f"UNIQUE constraint failed: {Album._meta.db_table}.serial_number"
        )

        with self.assertRaisesMessage(IntegrityError, expected_message):
            album_2.save()
