class LinkCls:
    name = ""
    direction = ""
    operator = None

    def __init__(self, name, direction, operator):
        self.name = name
        self.direction = direction
        self.operator = operator


class NodeCls:
    name = ""
    diagram = ""
    function = None
    parent = None
    links = []
    ref = None

    def getRef(self):
        return self.function(self.name)

    def __init__(self, name, diagram, function, parent, links):
        self.name = name
        self.function = function
        self.diagram = diagram
        self.parent = parent
        self.links = links


class ClusterCls:
    name = ""
    parent = None
    children = []
    links = []

    def __init__(self, name, parent, children, links):
        self.name = name
        self.children = children
        self.parent = parent
        self.links = links


class NodesDict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

