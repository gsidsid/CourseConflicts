def color_graph(graph):
    vertices = graph.get_vertices()
    if len(vertices) == 0:
        raise ValueError('Graph must have at least 1 vertex.')

    colored_vertices = dict()
    for num_colors in range(1, len(vertices)):
        colors = list(range(num_colors))
        for starting_vertex in vertices:
            if not _color_vertex(starting_vertex, graph, colors, colored_vertices):
                # Could not color subgraph starting at starting_vertex with the given number of colors
                break

    # Color all of the vertices in the graph object
    for vertex, color in colored_vertices.items():
        graph.color_vertex(vertex, color)

    return graph, colored_vertices


def _color_vertex(vertex, graph, colors, colored_vertices):
    # Try each color until one works
    for color in colors:
        # Try this color
        if _coloring_is_valid(vertex, color, graph, colored_vertices):
            # Coloring is valid, so save it
            colored_vertices[vertex] = color
            # Now color each child
            for child in graph.get_neighbors(vertex):
                # Skip over vertices that have already been colored
                if child in colored_vertices:
                    continue
                # Try to color this child and its neighbors, recursively
                if not _color_vertex(child, graph, colors, colored_vertices):
                    # Could not color subgraph with this color for the original vertex
                    # Break and try a new color for the original vertex
                    break
            else:  # (reached if the break statement above is not hit)
                # Successfully colored all nodes
                return True

    # Clear any saved but invalid color for this vertex
    if vertex in colored_vertices:
        del colored_vertices[vertex]

    # Unable to color the vertex with the given colors
    return False


def _coloring_is_valid(vertex, color, graph, colored_vertices):
    """Check if a potential coloring of a vertex is valid (i.e. not the same color as any of the neighbors)."""
    neighbors = graph.get_neighbors(vertex)

    # Check if any of the neighbors have this color
    for n in neighbors:
        # Get the color for the neighbor
        if colored_vertices.get(n) == color:
            # Neighbor has same color
            return False

    # No neighbors have same color
    return True


if __name__ == '__main__':
    from Graphing.graph import Graph
    from datetime import datetime
    graph = Graph()
    graph.add_edge('TellTheStory', 'Discrete')
    graph.add_edge('TellTheStory', 'FOCS')
    graph.add_edge('FOCS', 'Discrete')
    graph.add_edge('FOCS', 'CompArch')
    graph.add_edge('DBD', 'Discrete')
    graph.add_edge('DBD', 'TellTheStory')
    graph.add_edge('DBD', 'FunRobo')
    graph.add_edge('Transport', 'FunRobo')
    graph.add_edge('DBD', 'Transport')  # I
    graph.add_edge('TellTheStory', 'Transport')
    graph.add_edge('DBD', 'MechSolids')
    graph.add_edge('MechSolids', 'FunRobo')
    graph.add_edge('TellTheStory', 'MatSci')
    graph.add_edge('MatSci', 'CompArch')
    graph.add_edge('MatSci', 'DBD')
    graph.add_edge('MatSci', 'Discrete')
    graph.add_edge('DBD', 'FOCS')
    start_time = datetime.now()
    colored_graph, colored_vertices = color_graph(graph)
    elapsed_time = datetime.now() - start_time
    colors = set()
    for color in colored_vertices.values():
        colors.add(color)
    print('Colored {} vertices using {} colors in {}ms, like so:'.format(len(graph.get_vertices()), len(colors), elapsed_time.microseconds / 1000))
    print(colored_vertices)
