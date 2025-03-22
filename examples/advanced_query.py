from graphql_query_manager.introspection import fetch_introspection
from graphql_query_manager.query_generator import generate_graphql_query
import json

def main():
    # Fetch introspection data
    endpoint = "https://your-graphql-api.com/graphql"  # Replace with your actual GraphQL endpoint
    introspection_data = fetch_introspection(endpoint)
    if not introspection_data:
        print("Failed to fetch introspection data.")
        return

    # Parse introspection data to get fields
    parsed_schema = introspection_data.get("data", {}).get("__schema", {}).get("types", [])

    # Example of how to structure the fields for a more advanced query
    introspected_fields = {
        "user": [
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
                    "title",
                    {
                        "item": [
                            "name",
                            "price"
                        ]
                    }
                ]
            }
        ]
    }

    # Generate GraphQL query
    query = generate_graphql_query(introspected_fields["user"], root="user", user_id=1)

    print("Generated GraphQL Query:")
    print(query)

if __name__ == "__main__":
    main()