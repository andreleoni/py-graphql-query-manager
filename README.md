# py-graphql-query-manager

A Python library for generating GraphQL queries from introspection data. This library simplifies the process of interacting with GraphQL APIs by providing utilities to fetch schema details and construct queries based on the available types and fields.

## Features

- Fetch GraphQL introspection data to understand the schema.
- Generate GraphQL queries from a JSON representation of fields.
- Easy integration with existing GraphQL APIs.

## Installation

You can install the library using pip:

```
pip install py-graphql-query-manager
```

## Usage

### Basic Usage

To fetch introspection data and generate a query, you can use the following code:

```python
from graphql_query_manager.introspection import fetch_introspection
from graphql_query_manager.query_generator import generate_graphql_query

# Fetch introspection data - specify your GraphQL endpoint
endpoint = "https://your-graphql-api.com/graphql"
introspection_data = fetch_introspection(endpoint)

# Define the fields you want to query
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
                "title"
            ]
        }
    ]
}

# Generate the GraphQL query
query = generate_graphql_query(introspected_fields["user"], root="user", user_id=1)
print(query)
```

### Advanced Query Generation

For more complex queries, you can customize the JSON structure to include nested fields and relationships as needed.

```python
from graphql_query_manager.introspection import fetch_introspection
from graphql_query_manager.query_generator import generate_graphql_query

# Fetch introspection data
endpoint = "https://your-graphql-api.com/graphql"
introspection_data = fetch_introspection(endpoint)

# Extract schema information
parsed_schema = introspection_data["data"]["__schema"]
query_root = parsed_schema["queryType"]["name"]

# Define a complex query structure
query_fields = [
    {
        "user": [
            "id",
            "name",
            "email",
            {
                "posts": [
                    "id",
                    "title",
                    "content",
                    {
                        "comments": [
                            "id",
                            "text",
                            {
                                "author": [
                                    "name",
                                    "email"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

# Generate the GraphQL query
query = generate_graphql_query(query_fields, root=query_root, user_id=1)
print(query)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Changelog

See the CHANGELOG.md file for a history of changes and updates to the project.