import json
from graphql_query_manager.introspection import fetch_introspection
from graphql_query_manager.query_generator import generate_graphql_query

def main():
    # Fetch introspection data
    endpoint = "https://your-graphql-api.com/graphql"  # Replace with your actual GraphQL endpoint
    introspection_data = fetch_introspection(endpoint)

    if introspection_data:
        # Parse the introspection data to get the fields
        parsed_schema = introspection_data["data"]["__schema"]
        query_root = parsed_schema["queryType"]["name"]

        # Example fields to generate a query
        introspected_fields = {
            query_root: [
                {
                    "user": [
                        "id",
                        "name",
                        {
                            "posts": [
                                "title",
                                "content"
                            ]
                        }
                    ]
                }
            ]
        }

        # Generate a GraphQL query
        query = generate_graphql_query(introspected_fields[query_root], root=query_root, user_id=1)

        # Print the generated query
        print("Generated GraphQL Query:")
        print(query)
    else:
        print("Failed to fetch introspection data.")

if __name__ == "__main__":
    main()