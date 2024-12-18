import unittest
from calculator import FinancialCalculator

class TestFinancialCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = FinancialCalculator()

    def test_add_income(self):
        self.calculator.add_income(1000, "Salary")
        self.assertEqual(self.calculator.balance, 1000)

    def test_add_expense(self):
        self.calculator.add_income(1000, "Salary")
        self.calculator.add_expense(500, "Groceries")
        self.assertEqual(self.calculator.balance, 500)

    def test_negative_income(self):
        with self.assertRaises(ValueError):
            self.calculator.add_income(-100)

    def test_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.calculator.add_expense(100)

    def test_transactions(self):
        self.calculator.add_income(1000, "Salary")
        self.calculator.add_expense(500, "Groceries")
        transactions = self.calculator.get_transactions_as_list()  # Используем метод, возвращающий список
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["description"], "Salary")
        self.assertEqual(transactions[1]["description"], "Groceries")


if __name__ == "__main__":
    unittest.main()
