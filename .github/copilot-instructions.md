# GitHub Copilot Instructions for graph_utils

## Repository Overview

This is `graph_utils`, a Python library that provides utility functions and data structures for working with graphs. The library focuses on creating intuitive graph representations with support for arbitrary attributes on both nodes and edges through a `meta` attribute system.

**Key Information:**
- **Language**: Python 3.6+
- **License**: MIT
- **Status**: Early development (v0.0.1, Alpha)
- **Maintainer**: Anthony Sifontes
- **Package Structure**: Standard Python package with `src/graph_utils/` layout

## Project Structure

```
graph_utils/
├── src/graph_utils/
│   ├── __init__.py          # Package initialization
│   ├── structs.py           # Core classes: Node, Edge, Graph
│   └── traversal.py         # Graph traversal algorithms
├── .github/
│   └── copilot-instructions.md
├── pyproject.toml           # Project configuration
├── README.md               # Project documentation
└── LICENSE                 # MIT License
```

## Core Components

### Data Structures (`structs.py`)
- **Node**: Represents a graph node with a value and edges
- **Edge**: Represents a connection between two nodes with optional value
- **Graph**: Container for nodes and edges with management methods
- **SupportedValueType**: Union type for node/edge values (float, int, str, bool, None)

### Algorithms (`traversal.py`)
- **breadth_first()**: Implemented breadth-first traversal
- **dfs()**: Depth-first search (placeholder)
- **dijkstra()**: Dijkstra's shortest path (placeholder)
- **bellman_ford()**: Bellman-Ford algorithm (placeholder)
- **prim()**: Prim's MST algorithm (placeholder)
- **kruskal()**: Kruskal's MST algorithm (placeholder)
- **a_star()**: A* search algorithm (placeholder)

## Coding Standards

### Python Style
- Follow PEP 8 conventions
- Use type hints throughout (already established pattern)
- Import annotations from `__future__` for forward references
- Use descriptive variable names and comprehensive docstrings
- Maintain the existing Union type pattern for supported values

### Documentation Style
- Use triple-quoted docstrings for all classes and functions
- Follow the established pattern: `"""Brief description."""`
- Include parameter descriptions for complex functions
- Document return types and exceptions where applicable

### Code Organization
- Keep core data structures in `structs.py`
- Place algorithms in `traversal.py`
- Group related functionality together
- Use clear, descriptive names for methods and variables

## Development Guidelines

### Adding New Features

#### New Data Structures
- Add to `structs.py`
- Follow the established pattern with type hints
- Include comprehensive docstrings
- Consider metadata support via `meta` attribute if applicable

#### New Algorithms
- Add to `traversal.py`
- Include proper docstring with algorithm description
- Use type hints for parameters and return values
- Consider performance implications for large graphs
- Implement error handling for edge cases

#### Algorithm Implementation Pattern
```python
def algorithm_name(graph: Graph, start_node: Node, *args) -> ReturnType:
    """Brief description of the algorithm.
    
    Args:
        graph: The graph to operate on
        start_node: Starting node for traversal
        *args: Additional algorithm-specific parameters
    
    Returns:
        Description of return value
        
    Raises:
        Specific exceptions that might be raised
    """
    # Implementation here
```

### Code Quality

#### Type Safety
- Always use type hints for function parameters and return values
- Stick to the established `SupportedValueType` for node/edge values
- Use proper imports from `typing` module when needed

#### Error Handling
- Use appropriate Python exceptions (ValueError, TypeError, etc.)
- Provide clear error messages
- Handle edge cases gracefully
- Follow the pattern established in existing code (e.g., `remove_edge` raises ValueError)

#### Performance Considerations
- Consider time and space complexity for graph algorithms
- Be mindful of large graph performance
- Document complexity in algorithm docstrings where relevant

## Common Patterns

### Node Management
```python
# Creating nodes with values
node = Node(value="example")

# Adding edges between nodes
node1.add_edge(node2)
graph.add_edge(node1, node2)
```

### Graph Traversal Setup
```python
# Mark nodes as visited
node.visited = True

# Use queue/stack for traversal
queue = [start_node]
```

### Metadata Usage
The library supports arbitrary metadata on nodes and edges:
```python
node.meta = {"arbitrary": "attribute", "foo": "bar"}
edge.meta = {"weight": 5, "type": "directed"}
```

## Testing Guidelines

Currently, the repository does not have a test suite. When adding tests:
- Create a `tests/` directory in the repository root
- Use `pytest` as the testing framework
- Test both functionality and edge cases
- Include tests for algorithm correctness
- Test error conditions and exception handling

## Dependencies

The project currently has minimal dependencies:
- Python 3.6+ (specified in pyproject.toml)
- No external runtime dependencies
- Development dependencies should be added to pyproject.toml as needed

## TODO Items & Improvement Areas

Based on the codebase comments, focus on these areas:
1. **Type Enforcement**: Add support for enforcing types of node and edge values
2. **String Representations**: Add `__repr__` and `__str__` methods for better debugging
3. **Graph Creation**: Add class methods for creating graphs from edge/node lists
4. **Algorithm Implementations**: Complete the placeholder algorithms in `traversal.py`
5. **Testing**: Add comprehensive test suite
6. **Documentation**: Expand docstrings and add usage examples

## Best Practices for Contributors

1. **Maintain Simplicity**: The library aims to be easy to understand mentally
2. **Preserve Metadata Support**: Keep the flexible attribute system via `meta`
3. **Follow Existing Patterns**: Match the coding style already established
4. **Think About User Experience**: Make the API intuitive and discoverable
5. **Document Everything**: Comprehensive docstrings are essential
6. **Consider Performance**: Graph algorithms can be computationally expensive

## When Implementing New Algorithms

1. Research the algorithm thoroughly
2. Consider the input/output requirements
3. Plan for different graph representations (directed/undirected, weighted/unweighted)
4. Think about memory usage for large graphs
5. Add proper error handling
6. Include algorithmic complexity in documentation
7. Test with various graph sizes and structures

Remember: This library loves its users and wants them to be happy! Keep the API intuitive and the code readable.