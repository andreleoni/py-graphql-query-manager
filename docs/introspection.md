# Introspection Functionality in GraphQL Query Manager

## Overview

The introspection feature of the GraphQL Query Manager library allows users to retrieve detailed information about the schema of a GraphQL API. This includes the types, fields, and relationships available for querying. By leveraging GraphQL's introspection capabilities, developers can dynamically understand the structure of the API and generate queries accordingly.

## Fetching Introspection Data

To fetch introspection data, the library provides the `fetch_introspection` function. This function sends a GraphQL introspection query to the specified endpoint and returns the schema details in JSON format.

### Example Usage

```python
from graphql_query_manager.introspection import fetch_introspection

introspection_data = fetch_introspection()
if introspection_data:
    print(introspection_data)
else:
    print("Failed to fetch introspection data.")
```

## Parsing Introspection Data

Once the introspection data is retrieved, it can be parsed to extract the available query fields and their types. The `parse_introspection` function processes the introspection JSON and organizes the fields into a structured format that can be easily used for query generation.

### Example of Parsed Structure

The parsed structure will typically look like this:

```json
{
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
```

## Conclusion

The introspection functionality in the GraphQL Query Manager library provides a powerful way to interact with GraphQL APIs. By understanding the schema through introspection, developers can create dynamic and flexible queries tailored to their application's needs.