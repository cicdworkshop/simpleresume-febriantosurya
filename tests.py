"""This file is the unit test for SimpleResume web application.
"""
from users import User
import unittest


class TestUser(unittest.TestCase):
    """Class containing unit test for User object
    """
    def setUp(self):
        """Initialization of user object.
        """
        self.user = User()
        self.user.experiences = [
            {"start_date": "2016-01-01"},
            {"start_date": "2017-01-01"},
            {"start_date": "2018-01-01"},
            {"start_date": "2019-01-01"}                   
        ]
        self.user.certifications = [
            {"date": "2018-06-01"},
            {"date": "2019-02-01"},
            {"date": "2019-11-01"},
            {"date": "2020-07-01"}
        ]


    def test_sort_user_experience(self):
        """Test function: sort_user_experience
        """
        expected_result = [
            {"start_date": "2019-01-01"},
            {"start_date": "2018-01-01"},
            {"start_date": "2017-01-01"},
            {"start_date": "2016-01-01"}
        ]

        certifications_expected_result = [
            {"date": "2020-07-01"},
            {"date": "2019-11-01"},
            {"date": "2019-02-01"},
            {"date": "2018-06-01"}            
        ]

        self.user.sort_user_experience()
        self.user.sort_user_certifications()
        self.assertEqual(self.user.certifications, certifications_expected_result)
        self.assertEqual(self.user.experiences, expected_result)                      


    # (FOR WORKSHOP)
    # Implement the unit test for the function that you just created to sort the certifications.
    # Use the same logic as the test function above


if __name__ == "__main__":
    unittest.main()
