import unittest
from unittest.mock import MagicMock
# from bank_account import BankAccount, InterestRateComputer


class TestBackend(unittest.TestCase):
    def test(self):
        pass

    # def setUp(self):
    #     self.a1 = BankAccount(1000, "Chris")
    #     self.a2 = BankAccount(1500, "Hyacinth")
    #     self.a3 = BankAccount(1000, "Daniel")

    # def tearDown(self):
    #     self.a1 = None
    #     self.a2 = None
    #     self.a3 = None

    # def test_deposit(self):
    #     bal = self.a1.balance
    #     self.assertEqual(bal, 1000)
    #     self.assertEqual(self.a1.name, "Chris")
    #     self.a1.deposit(500)
    #     self.assertEqual(self.a1.balance, 1500)

    # def test_withdrawal(self):
    #     bal = self.a2.balance
    #     self.assertEqual(bal, 1500)
    #     self.a2.withdraw(1000)
    #     self.assertEqual(self.a2.balance, 500)
    #     #TODO: Add test for insufficient balance case

    # def test_EqualAccounts(self):
    #     self.assertTrue(self.a1.balance > 0)
    #     self.assertIsNot(self.a1, self.a2)
    #     self.assertIs(self.a1, self.a1)
      
    # def test_interest(self):
    #     interest_computer_mock = InterestRateComputer()
    #     interest_computer_mock.get_rate = MagicMock(interest_computer_mock, return_value = 0.02)
    #     self.assertEqual(self.a1.interest(interest_computer_mock),
    #                      self.a1.balance * 0.02)
        

if __name__ == "__main__":
    unittest.main()