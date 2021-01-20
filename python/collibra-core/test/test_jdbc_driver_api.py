"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.jdbc_driver_api import JDBCDriverApi  # noqa: E501


class TestJDBCDriverApi(unittest.TestCase):
    """JDBCDriverApi unit test stubs"""

    def setUp(self):
        self.api = JDBCDriverApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_jdbc_drivers(self):
        """Test case for find_jdbc_drivers

        Find JDBC Drivers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()