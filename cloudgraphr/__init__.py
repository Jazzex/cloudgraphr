import logging
import azure.functions as func
import mimetypes
import json
import operator
from diagrams import Diagram

import diagrams.azure.compute as compute
import diagrams.azure.database as database
import diagrams.azure.network as network

class AllNodesDict(dict):  
  
    # __init__ function  
    def __init__(self):  
        self = dict()  
          
    # Function to add key:value  
    def add(self, key, value):  
        self[key] = value  

all_nodes = AllNodesDict()

def get_diagram_type(typeStr):
    if typeStr == 'compute':
        return compute
    if typeStr == 'database':
        return database
    if typeStr == 'network':
        return network

def get_link_operator(link_type):
    if link_type == 'left':
        return operator.lshift
    if link_type == 'right':
        return operator.rshift
    if link_type == 'undirected' or link_type == "":
        return operator.sub

def get_func(typeStr):
    type_split = typeStr.split('.')
    diagram_type = get_diagram_type(type_split[0])
    attr = getattr(diagram_type, type_split[1])
    return attr

def run_diagram(req_dict):
    with Diagram(req_dict['name'], show=False):
        for node in req_dict['nodes']:
            node_name = str(node['node_name'])
            node_type = str(node['node_type'])
            node_function = get_func(node_type)
            node_defined = node_function(node_name)
            print(node_name, node_defined)
            all_nodes.add(node_name, node_defined)
        for link in req_dict['links']:
            if link["from_node"] in all_nodes and link["to_node"] in all_nodes:
                op = get_link_operator(link["dir"])
                from_node = all_nodes[link["from_node"]]
                to_node = all_nodes[link["to_node"]]
                print(op, from_node, to_node)
                op(from_node, to_node)
                
def main(req: func.HttpRequest) -> func.HttpResponse:
    global nodes
    all_nodes = {}
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_body()
        req_dict = json.loads(req_body)
        run_diagram(req_dict)
        filename = f"{req_dict['name']}.png"
        with open(filename, 'rb') as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
    except Exception as e:
        logging.info(e)
        print(e)
        headers = {
            "Content-type": "text/plain",
            "Access-Control-Allow-Origin": "*"
        }
        return func.HttpResponse("Something went wrong!", status_code=500, headers=headers)

