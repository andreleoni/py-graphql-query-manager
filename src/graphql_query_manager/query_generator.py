def generate_graphql_query(fields, root="user", user_id=1):
    def build_field_string(field_structure):
        query_parts = []
        for field in field_structure:
            if isinstance(field, dict):  # Caso o campo seja um dicionário (subcampo)
                for key, value in field.items():
                    sub_query = build_field_string(value)  # Recursão para sub-campos
                    query_parts.append(f"{key} {{ {sub_query} }}")  # Adiciona o subcampo com as chaves
            else:
                query_parts.append(field)  # Campo simples
        return " ".join(query_parts)

    query_fields = build_field_string(fields)

    # Corrigindo para usar user_id como parâmetro em vez de id
    graphql_query = f"""
    {{
      {root}(user_id: "{user_id}") {{
        {query_fields}
      }}
    }}
    """

    return graphql_query.strip()