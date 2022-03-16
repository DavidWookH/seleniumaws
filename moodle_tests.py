import unittest
import moodle_locator as locators
import moodle_methods as methods

class MoodleAppPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest that is function inside class (vs @classmethod)
    def test_create_new_user(): # test_in the name is mandatory
        methods.setUp()
        methods.log_in(locators.admin_name, locators.admin_password)  # Login# Launch app
        methods.create_new_user()  # check_new_user_can_login()
        methods.search_user()
        methods.log_out()  # logout
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()
        methods.log_in(locators.admin_name,locators.admin_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()



