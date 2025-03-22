# py-graphql-query-manager documentation

## Overview

The `py-graphql-query-manager` is a Python library designed to facilitate interaction with GraphQL APIs by providing tools for introspection and query generation. This library allows developers to easily fetch schema details and construct queries based on the available types and fields in a GraphQL service.

## Features

- **Introspection**: Automatically fetch and parse the GraphQL schema to understand the available queries, types, and fields.
- **Query Generation**: Generate GraphQL query strings from a structured JSON representation of fields, making it easy to construct complex queries programmatically.
- **Utility Functions**: Includes various utility functions to assist with data processing and handling common tasks related to GraphQL interactions.

## Installation

To install the library, you can use pip:

```
pip install py-graphql-query-manager
```

## Usage

### Basic Introspection

To fetch introspection data from a GraphQL API, you can use the `fetch_introspection` function:

```python
from graphql_query_manager.introspection import fetch_introspection

introspection_data = fetch_introspection()
```

### Generating a Query

Once you have the introspection data, you can generate a GraphQL query using the `generate_graphql_query` function:

```python
from graphql_query_manager.query_generator import generate_graphql_query

fields = {
    "user": [
        "name",
        "email",
        {
            "posts": [
                "title",
                "content"
            ]
        }
    ]
}

query = generate_graphql_query(fields, root="user", user_id=1)
```

## Documentation

For more detailed information on specific functionalities, please refer to the following sections:

- [Introspection](introspection.md): Learn how to use the introspection features of the library.
- [Query Generation](query_generation.md): Understand how to construct queries using the provided tools.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the library.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.