import unittest
from graphql_query_manager.introspection import fetch_introspection
import json

class TestIntrospection(unittest.TestCase):

    def test_fetch_introspection_success(self):
        # Simulate a successful introspection response
        response_data = {
            "data": {
                "__schema": {
                    "queryType": {
                        "name": "Query"
                    },
                    "types": [
                        {
                            "name": "User",
                            "kind": "OBJECT",
                            "fields": [
                                {
                                    "name": "id",
                                    "type": {
                                        "name": "ID",
                                        "kind": "SCALAR"
                                    }
                                },
                                {
                                    "name": "name",
                                    "type": {
                                        "name": "String",
                                        "kind": "SCALAR"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }

        # Mock the requests.post method to return the simulated response
        with unittest.mock.patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = response_data
            
            introspection_data = fetch_introspection()
            self.assertIsNotNone(introspection_data)
            self.assertEqual(introspection_data['data']['__schema']['queryType']['name'], 'Query')

    def test_fetch_introspection_failure(self):
        # Simulate a failed introspection response
        with unittest.mock.patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 500
            
            introspection_data = fetch_introspection()
            self.assertIsNone(introspection_data)

if __name__ == '__main__':
    unittest.main()