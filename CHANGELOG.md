# CHANGELOG

## [Unreleased]
### Added
- Initial implementation of the GraphQL query manager library.
- Functionality for fetching GraphQL introspection data.
- Functionality for generating GraphQL queries from JSON structures.

## [0.1.0] - 2023-10-01
### Added
- Basic structure of the project with necessary files and directories.
- `fetch_introspection` function in `introspection.py` to retrieve schema details.
- `generate_graphql_query` function in `query_generator.py` to create GraphQL queries.

### Changed
- Updated README.md with project description and usage instructions.

### Fixed
- Resolved initial bugs in introspection fetching and query generation logic.

## [0.1.1] - 2023-10-15
### Added
- Unit tests for introspection and query generation in `tests/test_introspection.py` and `tests/test_query_generator.py`.
- Sample JSON data for testing in `tests/fixtures/schema_data.json`.

### Changed
- Improved error handling in `fetch_introspection` function.

## [0.2.0] - 2023-10-30
### Added
- Documentation for introspection and query generation in the `docs` directory.
- Examples demonstrating basic and advanced usage of the library in the `examples` directory.

### Changed
- Refined the structure of the generated GraphQL queries for better readability.

### Fixed
- Minor bugs and performance improvements based on user feedback.