import requests
import json

GRAPHQL_ENDPOINT = "http://localhost:4000/"

def fetch_introspection():
    """Fetches the GraphQL introspection data to retrieve schema details and available types."""
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
    response = requests.post(GRAPHQL_ENDPOINT, json={"query": introspection_query})
    return response.json() if response.status_code == 200 else None