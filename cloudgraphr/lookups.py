import diagrams.azure.compute as compute
import diagrams.azure.database as database
import diagrams.azure.network as network
import diagrams.azure.general as general
import diagrams.azure.analytics as analytics
import diagrams.azure.iot as iot
import diagrams.azure.security as security
import diagrams.azure.web as web
import diagrams.saas.identity as identity
import operator


def get_diagram_type(typeStr):
    if typeStr == "compute":
        return compute
    if typeStr == "database":
        return database
    if typeStr == "network":
        return network
    if typeStr == "general":
        return general
    if typeStr == "analytics":
        return analytics
    if typeStr == "iot":
        return iot
    if typeStr == "security":
        return security
    if typeStr == "web":
        return web
    if typeStr == "identity":
        return identity


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
