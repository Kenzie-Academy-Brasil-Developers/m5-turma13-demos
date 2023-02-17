from rest_framework.test import APITestCase
from accounts.models import Account
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import status
from pytest_check import check
from books.models import Book


class BookViewTest(APITestCase):
    """
    1. Se alguem sem token consegue criar livro
    2. Se alguem com token inválido consegue criar livro
    3. Se alguem com token valido porém sem permissao consegue criar livro
    4. Se alguem com token válido e body inválido consegue criar livro
    5. Se alguem com token válido e body válido consegue criar livro
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/books/"

        # superuser
        cls.super_user = Account.objects.create_superuser(
            username="super1",
            password="1234",
        )
        super_user_token = RefreshToken.for_user(cls.super_user)
        cls.super_user_access_token = str(super_user_token.access_token)

        # non superuser
        cls.common_user = Account.objects.create_user(
            username="common1",
            password="1234",
        )
        common_user_token = RefreshToken.for_user(cls.common_user)
        cls.common_user_access_token = str(common_user_token.access_token)

    def test_book_creation_without_token(self):
        book_data = {
            "title": "Book 1",
            "published_date": "1993-03-03",
        }

        response = self.client.post(self.BASE_URL, data=book_data, format="json")

        # STATUS CODE TEST
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code
        message = (
            f"Verifique se o status code retornado do POST "
            + f"em {self.BASE_URL} sem token é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, message)

    def test_book_creation_with_superuser_token_and_valid_book_data(self):
        book_data = {
            "title": "Book 1",
            "published_date": "1993-03-03",
        }
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.super_user_access_token
        )
        response = self.client.post(self.BASE_URL, data=book_data, format="json")

        """
        with self.subTest():
            # RETURNED BODY TEST
            resulted_data = response.json()
            expected_data = {
                "id": 1000,
                "title": book_data["title"],
                "published_date": book_data["published_date"],
                "book_owner": self.super_user.username,
            }
            message = (
                f"Verifique se o body retornado do POST "
                + f"em {self.BASE_URL} com token de superuser e dados válidos está correto"
            )

            self.assertDictEqual(expected_data, resulted_data, message)

         with self.subTest():
            # STATUS CODE TEST
            # expected_status_code = status.HTTP_201_CREATED
            expected_status_code = status.HTTP_400_BAD_REQUEST
            resulted_status_code = response.status_code
            message = (
                f"Verifique se o status code retornado do POST "
                + f"em {self.BASE_URL} com token de superuser e dados válidos é {expected_status_code}"
            )

            self.assertEqual(expected_status_code, resulted_status_code, message)
        """
        with check:
            # STATUS CODE TEST
            expected_status_code = status.HTTP_201_CREATED
            # expected_status_code = status.HTTP_400_BAD_REQUEST
            resulted_status_code = response.status_code
            message = (
                f"Verifique se o status code retornado do POST "
                + f"em {self.BASE_URL} com token de superuser e dados válidos é {expected_status_code}"
            )

            self.assertEqual(expected_status_code, resulted_status_code, message)

        with check:
            # RETURNED BODY TEST
            resulted_data = response.json()
            inserted_book = Book.objects.first()
            expected_data = {
                "id": inserted_book.pk,
                "title": book_data["title"],
                "published_date": book_data["published_date"],
                "book_owner": self.super_user.username,
            }
            message = (
                f"Verifique se o body retornado do POST "
                + f"em {self.BASE_URL} com token de superuser e dados válidos está correto"
            )

            self.assertDictEqual(expected_data, resulted_data, message)
