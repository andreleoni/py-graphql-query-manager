# Query Generation Functionality

This document provides an overview of the query generation functionality in the `py-graphql-query-manager` library. It explains how to construct GraphQL queries from a JSON structure representing the fields and their relationships.

## Overview

The `generate_graphql_query` function is designed to take a JSON representation of the fields you want to query and produce a valid GraphQL query string. This allows users to dynamically create queries based on the introspection data retrieved from a GraphQL API.

## Function Signature

```python
generate_graphql_query(fields: dict, root: str = "user", user_id: int = 1) -> str
```

### Parameters

- **fields**: A dictionary representing the fields to be queried. This structure should reflect the hierarchy of the GraphQL schema.
- **root**: A string representing the root query type (default is "user"). This is the entry point for the query.
- **user_id**: An integer representing the user ID to be used in the query (default is 1).

### Returns

- A string containing the constructed GraphQL query.

## Example Usage

Here’s a simple example of how to use the `generate_graphql_query` function:

```python
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

query = generate_graphql_query(introspected_fields["user"], root="user", user_id=1)
print(query)
```

### Output

The above example would produce a query string similar to:

```
{
  user(user_id: "1") {
    bank {
      available_withdraw
      future_deposit {
        amount
      }
    }
    purchases {
      amount_paid
      title
    }
  }
}
```

## Conclusion

The `generate_graphql_query` function provides a flexible way to construct GraphQL queries based on introspection data. By using a JSON structure to represent the desired fields, users can easily create complex queries tailored to their needs.