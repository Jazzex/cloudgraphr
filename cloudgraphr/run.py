import logging, json, mimetypes, os, sys, time
import azure.functions as func
from diagrams import Diagram, Cluster, Node
from .lookups import get_func, get_link_operator
from .classes import NodesDict, ClusterCls, NodeCls
from .maps import map_node, map_cluster
import jsonpickle

sys.path.append(os.path.abspath("/home/site/wwwroot/cloudgraphr"))
all_nodes = {}


def map_entities(req_dict):
    entities = []
    with Diagram(req_dict["name"], show=False):
        for entity in req_dict["graph"]:
            if entity["type"] == "node":
                entities.append(map_node(entity))
            if entity["type"] == "cluster":
                entities.append(map_cluster(entity))
        create_entities(entities)
        create_links()


def create_entities(entities):
    global all_nodes
    for entity in entities:
        if (isinstance(entity, ClusterCls)):
            with Cluster(entity.name):
                create_entities(entity.children)
        elif (isinstance(entity, NodeCls)):
            node = entity
            node.set_ref()
            all_nodes[node.name] = node


def create_links():
    for node_name in all_nodes:
        node = all_nodes[node_name]
        for link in node.links:
            link.operator(node.ref, all_nodes[link.name].ref)


def main(req: func.HttpRequest) -> func.HttpResponse:
    global all_nodes
    all_nodes = {}
    logging.info("Python HTTP trigger function processed a request.")
    try:
        req_body = req.get_body()
        req_dict = json.loads(req_body)
        map_entities(req_dict)
        # dumped = jsonpickle.encode(clusters)
        # headers = {
        #     "Content-type": "application/json",
        #     "Access-Control-Allow-Origin": "*",
        # }
        # return func.HttpResponse(dumped, status_code=200, headers=headers)

        filename = f"{req_dict['name']}.png"
        with open(filename, "rb") as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
    except Exception as e:
        logging.info(e)
        print(e)
        headers = {"Content-type": "text/plain", "Access-Control-Allow-Origin": "*"}
        return func.HttpResponse(
            "Something went wrong!", status_code=500, headers=headers
        )
