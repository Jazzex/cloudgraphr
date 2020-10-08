from .classes import NodeCls, ClusterCls, LinkCls
from .lookups import get_func, get_link_operator


def map_node(node_dict, parent=None):
    node_name = node_dict["name"]
    diagram = node_dict["diagram"]
    links_dict = node_dict["links"]
    links = []
    for link in links_dict:
        op = get_link_operator(link["direction"])
        for name in link['names']:
            links.append(LinkCls(name, link["direction"], op))

    node_function = get_func(diagram)
    return NodeCls(node_name, diagram, node_function, parent, links)


def map_cluster(cluster_dict, parent=None):
    children = []
    links = []
    name = cluster_dict["name"]

    for child in cluster_dict['children']:
        if (child['type'] == 'node'):
            children.append(map_node(child))
        if (child['type'] == 'cluster'):
            children.append(map_cluster(child))

    return ClusterCls(name, parent, children, links) 
