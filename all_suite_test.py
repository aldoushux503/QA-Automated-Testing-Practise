import unittest

from unittest.loader import makeSuite

from test_cases.add_player_test import TestAddPlayer
from test_cases.clear_add_player_page_test import TestClearPlayer
from test_cases.language_change_test import TestLanguageChange
from test_cases.login_to_the_system_test import TestLoginPage
from test_cases.login_with_invalid_data_test import TestInvalidLogin
from test_cases.sign_out_of_the_system_test import TestSignOut


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestClearPlayer))
    test_suite.addTest(makeSuite(TestLanguageChange))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestInvalidLogin))
    test_suite.addTest(makeSuite(TestSignOut))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
