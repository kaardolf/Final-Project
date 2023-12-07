"""test for functions"""

import unittest
from utility import utility


class TestDB(unittest.TestCase):
    """test class"""

    def tearDown(self) -> None:
        """deletes any test if failed"""
        utility.db_delte("TEST")
        utility.db_delte("TEST2")
        utility.db_delte("NEWTEST")

    def test_insert_one(self) -> None:
        """tests insert, read one, and delete"""
        num = utility.db_count()
        test_data = {
            "name": "TEST",
            "borough": "New York",
            "cuisine": "Food",
            "ave_rating": None,
            "ratings": [],
            "comments": []}  # type: ignore
        utility.db_insert_one(test_data)
        self.assertEqual(num+1, utility.db_count())
        data = utility.db_read_one("TEST")
        self.assertEqual(test_data, data)

        utility.db_delte("TEST")
        self.assertEqual(num, utility.db_count())

    def test_insert_many(self) -> None:
        """tests insert many"""
        num = utility.db_count()
        test_data = {
            "name": "TEST",
            "borough": "New York",
            "cuisine": "American",
            "ave_rating": None,
            "ratings": [],
            "comments": []}  # type: ignore
        test_data2 = {
            "name": "TEST2",
            "borough": "New York",
            "cuisine": "Mexican",
            "ave_rating": None,
            "ratings": [],
            "comments": []}  # type: ignore

        table = []
        table.append(test_data)
        table.append(test_data2)

        utility.db_insert_many(table)
        self.assertEqual(num+2, utility.db_count())

        data = utility.db_read_one("TEST")
        self.assertEqual(test_data, data)

        data = utility.db_read_one("TEST2")
        self.assertEqual(test_data2, data)

        utility.db_delte("TEST")
        utility.db_delte("TEST2")
        self.assertEqual(num, utility.db_count())

    def test_update(self) -> None:
        """test update"""

        num = utility.db_count()
        test_data = {
            "name": "TEST",
            "borough": "New York",
            "cuisine": "Food",
            "ave_rating": None,
            "ratings": [],
            "comments": []}  # type: ignore

        utility.db_insert_one(test_data)

        utility.db_update("TEST", "name", "NEWTEST")

        new_test = utility.db_read_one("NEWTEST")
        expected = {
            "name": "NEWTEST",
            "borough": "New York",
            "cuisine": "Food",
            "ave_rating": None,
            "ratings": [],
            "comments": []}  # type: ignore

        self.assertEqual(new_test['name'], expected['name'])
        self.assertEqual(new_test['borough'], expected['borough'])
        self.assertEqual(new_test['cuisine'], expected['cuisine'])
        self.assertEqual(new_test['ave_rating'], expected['ave_rating'])
        self.assertEqual(new_test['ratings'], expected['ratings'])
        self.assertEqual(new_test['comments'], expected['comments'])

        utility.db_delte("NEWTEST")
        self.assertEqual(num, utility.db_count())
