import requests
import json

def fetch_introspection(endpoint):
    """Fetches the GraphQL introspection data to retrieve schema details and available types.

    Args:
        endpoint (str): The GraphQL endpoint URL.

    Returns:
        dict: The introspection query response or None if the request fails.
    """
    introspection_query = """
    {
      __schema {
        queryType {
          name
        }
        types {
          name
          kind
          fields {
            name
            type {
              name
              kind
              ofType {
                name
                kind
              }
            }
          }
        }
      }
    }
    """
    response = requests.post(endpoint, json={"query": introspection_query})
    return response.json() if response.status_code == 200 else None