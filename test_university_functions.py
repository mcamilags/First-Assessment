import unittest
from unittest.mock import patch
from authentication import Authentication
from finances import Finances
from inventory import Inventory
from university_functions import UniversityFunctions
from user import User


class TestUniversityFunctions(unittest.TestCase):
    def setUp(self):
        self.authentication = Authentication()
        self.finances = Finances()
        self.inventory = Inventory()
        self.student_user = User("John Doe", "john@example.com", "123456", "password", "student")
        self.admin_user = User("Admin User", "admin@example.com", "789101", "admin_password", "admin")
        self.authentication.register_user(self.student_user)
        self.authentication.register_user(self.admin_user)

    def tearDown(self):
        self.authentication = None
        self.finances = None
        self.inventory = None
        self.student_user = None
        self.admin_user = None

    def test_rent_high_tech_computer(self):
        self.finances.open_account(self.student_user)
        self.inventory.resources["high-tech computer"] = 1

        with patch("builtins.input", side_effect=["1"]):
            output = UniversityFunctions.rent_high_tech_computer(self.student_user, self.finances, self.inventory)
        self.assertEqual(output, "High-tech computer rented successfully.")

    def test_reserve_bicycle(self):
        self.finances.open_account(self.student_user)
        self.inventory.resources["bicycle"] = 1

        with patch("builtins.input", side_effect=["1"]):
            output = UniversityFunctions.reserve_bicycle(self.student_user, self.finances, self.inventory)
        self.assertEqual(output, "Bicycle reserved successfully.")

    def test_make_cashless_payment(self):
        self.finances.open_account(self.student_user)
        self.finances.accounts[self.student_user.get_id()]["money"] = 20

        with patch("builtins.input", side_effect=["15"]):
            output = UniversityFunctions.make_cashless_payment(self.student_user, self.finances)
        self.assertEqual(output, "Payment of 15.0 made successfully.")

    def test_pay_for_food_with_qr_code(self):
        self.finances.open_account(self.student_user)
        self.finances.accounts[self.student_user.get_id()]["money"] = 30

        with patch("builtins.input", side_effect=["25"]):
            output = UniversityFunctions.pay_for_food_with_qr_code(self.student_user, self.finances)
        self.assertEqual(output, "Payment of 25.0 made successfully with QR code.")

    def test_access_virtual_library(self):
        output = UniversityFunctions.access_virtual_library(self.student_user)
        self.assertEqual(output, "Accessing virtual library...")

    def test_manage_services_and_loans(self):
        output = UniversityFunctions.manage_services_and_loans(self.admin_user)
        self.assertEqual(output, "You have administrative privileges to manage services and loans.")

    def test_manage_financial_transactions(self):
        output = UniversityFunctions.manage_financial_transactions(self.admin_user, self.finances)
        self.assertEqual(output, "Managing financial transactions...")

    def test_integrate_payment_methods(self):
        output = UniversityFunctions.integrate_payment_methods(self.admin_user)
        self.assertEqual(output, "Integrating payment methods...")

    def test_manage_inventory(self):
        output = UniversityFunctions.manage_inventory(self.admin_user)
        self.assertEqual(output, "Managing inventory...")


if __name__ == "__main__":
    unittest.main()
