"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import collibra_core
from collibra_core.api.asset_types_api import AssetTypesApi  # noqa: E501


class TestAssetTypesApi(unittest.TestCase):
    """AssetTypesApi unit test stubs"""

    def setUp(self):
        self.api = AssetTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_asset_type(self):
        """Test case for add_asset_type

        Add asset type  # noqa: E501
        """
        pass

    def test_add_asset_types(self):
        """Test case for add_asset_types

        Add multiple asset types  # noqa: E501
        """
        pass

    def test_change_asset_type(self):
        """Test case for change_asset_type

        Change asset type  # noqa: E501
        """
        pass

    def test_change_asset_types(self):
        """Test case for change_asset_types

        Change multiple asset types  # noqa: E501
        """
        pass

    def test_find_asset_types(self):
        """Test case for find_asset_types

        Find asset types matching criteria  # noqa: E501
        """
        pass

    def test_find_parent_types(self):
        """Test case for find_parent_types

        Find parent types  # noqa: E501
        """
        pass

    def test_find_sub_asset_types(self):
        """Test case for find_sub_asset_types

        Find asset subtypes  # noqa: E501
        """
        pass

    def test_get_asset_type(self):
        """Test case for get_asset_type

        Get asset type by ID  # noqa: E501
        """
        pass

    def test_remove_asset_type(self):
        """Test case for remove_asset_type

        Remove asset type by ID  # noqa: E501
        """
        pass

    def test_remove_asset_types(self):
        """Test case for remove_asset_types

        Remove multiple asset types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()