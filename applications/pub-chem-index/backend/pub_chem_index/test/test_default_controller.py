# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from pub_chem_index.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_ingest(self):
        """Test case for ingest

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/ingestion',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
