# coding:utf-8
from xmlrpc.server import SimpleXMLRPCServer  
from xmlrpc.client import ServerProxy
from node import get_nodes, add_node
from database import BlockChainDB, UnTransactionDB, TransactionDB
from lib.common import cprint
server = None

PORT = 8301

class RpcServer():

    def __init__(self,server):
        self.server = server

    def ping(self):
        return True
    
    def get_blockchain(self):
        bcdb = BlockChainDB()
        return bcdb.find_all()

    def new_block(self,block):
        cprint('RPC', block)
        BlockChainDB().insert(block)
        UnTransactionDB().clear()
        cprint('INFO',"Receive new block.")
        return True

    def get_transactions(self):
        tdb = TransactionDB()
        return tdb.find_all()

    def new_untransaction(self,untx):
        cprint(__name__,untx)
        UnTransactionDB().insert(untx)
        cprint('INFO',"Receive new unchecked transaction.")
        return True

    def blocked_transactions(self,txs):
        TransactionDB().write(txs)
        cprint('INFO',"Receive new blocked transactions.")
        return True

    def add_node(self, address):
        add_node(address)
        return True

class RpcClient():

    ALLOW_METHOD = ['get_transactions', 'get_blockchain', 'new_block', 'new_untransaction', 'blocked_transactions', 'ping', 'add_node']

    def __init__(self, node):
        self.node = node
        self.client = ServerProxy(node)
    
    def __getattr__(self, name):
        def noname(*args, **kw):
            if name in self.ALLOW_METHOD:
                return getattr(self.client, name)(*args, **kw)
        return noname

class BroadCast():

    def __getattr__(self, name):
        def noname(*args, **kw):
            cs = get_clients()
            rs = []
            for c in cs:
                try:
                    rs.append(getattr(c,name)(*args, **kw))
                except ConnectionRefusedError:
                    cprint('WARN', 'Contact with node %s failed when calling method %s , please check the node.' % (c.node,name))
                else:
                    cprint('INFO', 'Contact with node %s successful calling method %s .' % (c.node,name))
            return rs
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
        clients.append(RpcClient(node))
    return clients