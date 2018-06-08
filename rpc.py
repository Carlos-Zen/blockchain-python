# coding:utf-8
from xmlrpc.server import SimpleXMLRPCServer  
from xmlrpc.client import ServerProxy
from node import get_nodes, add_node
from database import BlockChainDB
server = None


PORT = 8301

class RpcServer():

    def __init__(self,server):
        self.server = server

    def ping(self):
        return True
    
    def get_blockchain(self):
        dbd = BlockChainDB()
        return []

    def add_block(self,block):
        pass

    def get_transactions(self):
        return []
    
    def get_nodes(self):
        return []

class BroadCast():
    def __getattr__(self,name):
        def noname():
            if name in ['new_block', 'new_transaction']:
                cs = get_clients()
                for c in cs: 
                    getattr(c,name)
        return noname

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