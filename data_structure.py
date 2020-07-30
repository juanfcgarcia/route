import networkx as nx
import read_txt as rt

def create_graph():
    graph = {}
    rt.read_txt()
    G = nx.Graph()
    vertices = rt.vertices
    edges = rt.edges
    G.add_nodes_from(vertices)
    G.add_weighted_edges_from(edges)
    nx.draw_networkx(G)
    graph = nx.to_dict_of_dicts(G)
    graph = change_format_dict(graph)
    return graph

def change_format_dict(grap):
    for n_key, n_data in grap.items():
        for key in n_data:
            n_data[key] = int(n_data[key]["weight"])
    return grap