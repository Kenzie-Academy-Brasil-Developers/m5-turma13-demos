from django.test import TestCase

# unittest


class TestExample(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print("=" * 100)
        print("setUpTestData executado")
        print("=" * 100)

        cls.my_value = 10

    def setUp(self) -> None:
        print("setUp executado")
        print("=" * 100)

    def tearDown(self) -> None:
        return super().tearDown()

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 100)
        print("tearDownClass executado")
        print("=" * 100)

    def test_if_my_value_is_equal_to_value_to_compare(self):
        """
        Teste que verifica se `my_value` é igual a `value_to_compare`
        """
        # my_value = 10
        value_to_compare = 10
        print("test_if_my_value_is_equal_to_value_to_compare executado")
        # asserts
        # self.assertTrue(my_value == value_to_compare)
        message = "Verifique se `my_value` é igual a `value_to_compare`"
        # self.assertEqual(my_value, value_to_compare, message)
        self.assertEqual(self.my_value, value_to_compare, message)

    def test_if_my_value_is_equal_to_value_to_compare_2(self):
        """
        Teste que verifica se `my_value` é igual a `value_to_compare_2`
        """
        # my_value = 10
        value_to_compare_2 = 10
        print("test_if_my_value_is_equal_to_value_to_compare_2 executado")
        message = "Verifique se `my_value` é igual a `value_to_compare_2`"
        self.assertEqual(self.my_value, value_to_compare_2, message)
        # self.assertEqual(my_value, value_to_compare_2, message)
