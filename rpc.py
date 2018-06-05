# coding:utf-8
from xmlrpc.server import SimpleXMLRPCServer  
from xmlrpc.client import ServerProxy
from node import get_nodes, add_node

server = None


PORT = 8301

class RpcServer():

    def __init__(self,server):
        self.server = server

    def ping(self):
        return True
    
    def get_blockchain(self):
        return []

    def get_transactions(self):
        return []
    
    def get_nodes(self):
        return []

def start_server(ip, port=8301):
    server = SimpleXMLRPCServer((ip, port))
    rpc = RpcServer(server)
    server.register_instance(rpc)
    server.serve_forever()

def get_clients():
    clients = []
    nodes = get_nodes()
    for node in nodes:
        clients.append(ServerProxy(node))
    return clients