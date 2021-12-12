from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, a, b, directed=False):
        self.edges[a].append(b)
        if not directed:
            self.edges[b].append(a)

    def find_all_paths(self, start, end, node_filter=None):
        paths = []
        incomplete_paths = [[start]]

        while incomplete_paths:
            path = incomplete_paths.pop()
            prev_node = path[-1]
            for candidate in self.edges[prev_node]:
                if candidate == end:
                    p = list(path)
                    p.append(candidate)
                    paths.append(p)
                elif node_filter:
                    if node_filter(self, path, candidate):
                        p = list(path)
                        p.append(candidate)
                        incomplete_paths.append(p)
                elif candidate not in path:
                    p = list(path)
                    p.append(candidate)
                    incomplete_paths.append(p)

        return paths
