import diagrams.azure.compute as compute
import diagrams.azure.database as database
import diagrams.azure.network as network
import operator


def get_diagram_type(typeStr):
    if typeStr == "compute":
        return compute
    if typeStr == "database":
        return database
    if typeStr == "network":
        return network


def get_link_operator(link_type):
    if link_type == "left":
        return operator.lshift
    if link_type == "right":
        return operator.rshift
    if link_type == "undirected" or link_type == "":
        return operator.sub


def get_func(typeStr):
    type_split = typeStr.split(".")
    diagram_type = get_diagram_type(type_split[0])
    attr = getattr(diagram_type, type_split[1])
    return attr
