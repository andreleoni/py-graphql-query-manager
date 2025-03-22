import json
import unittest
from graphql_query_manager.query_generator import generate_graphql_query

class TestQueryGenerator(unittest.TestCase):

    def test_generate_graphql_query_simple(self):
        fields = [
            "name",
            "age"
        ]
        expected_query = """
        {
          user(user_id: "1") {
            name age
          }
        }""".strip()
        query = generate_graphql_query(fields, root="user", user_id=1)
        self.assertEqual(query, expected_query)

    def test_generate_graphql_query_with_subfields(self):
        fields = [
            {
                "bank": [
                    "available_withdraw",
                    {
                        "future_deposit": [
                            "amount"
                        ]
                    }
                ]
            },
            {
                "purchases": [
                    "amount_paid",
                    "title"
                ]
            }
        ]
        expected_query = """
        {
          user(user_id: "1") {
            bank {
              available_withdraw future_deposit { amount }
            }
            purchases {
              amount_paid title
            }
          }
        }""".strip()
        query = generate_graphql_query(fields, root="user", user_id=1)
        self.assertEqual(query, expected_query)

    def test_generate_graphql_query_empty_fields(self):
        fields = []
        expected_query = """
        {
          user(user_id: "1") {
          }
        }""".strip()
        query = generate_graphql_query(fields, root="user", user_id=1)
        self.assertEqual(query, expected_query)

if __name__ == '__main__':
    unittest.main()